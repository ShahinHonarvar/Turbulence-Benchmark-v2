import re

def palindromes_between_indices(s: str) -> set:
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = s[3:8]
    s = ''.join((c for c in s if c in alphabet))
    palindromes = {p for i in range(6, len(s) + 1) for p in {s[j:i + j] for j in range(len(s) - i + 1)} if p == p[::-1]}
    return palindromes
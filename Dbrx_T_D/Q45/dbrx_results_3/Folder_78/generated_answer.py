from collections import defaultdict
import re

def palindromes_between_indices(s):
    eng_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = s[6:9]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i, len(substr)):
            candidate = substr[i:j + 1]
            if candidate and candidate == candidate[::-1] and set(candidate).issubset(eng_letters):
                palindromes.add(candidate.lower())
    return {p for p in palindromes if len(p) >= 3}
import re
    from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for start in range(len(s) - 3):
        for end in range(start + 3, min(start + 7, len(s))):
            if s[start:end + 1] and set(s[start:end + 1]).issubset(english_letters):
                palindromes.add(s[start:end + 1])
    return {p for p in palindromes if p == p[::-1]}
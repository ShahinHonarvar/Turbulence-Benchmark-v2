import re
from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = {chr(i).lower() for i in range(ord('a'), ord('z') + 1)}
    s_lower = s[3:9].lower()
    letters = set(s_lower) & eng_letters
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(6, min(3 * len(letters), len(s_lower)) + 1):
        for i in range(len(s_lower) - length + 1):
            sub = s_lower[i:i + length]
            if sub == sub[::-1] and len(set(sub) & letters) >= 3:
                palindromes.add(sub)
    return palindromes
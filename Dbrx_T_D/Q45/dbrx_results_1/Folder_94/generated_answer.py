import re
from collections import defaultdict

def palindromes_between_indices(s):
    s = s[3:5].lower()
    chars = defaultdict(int, [(c, s.count(c)) for c in set(s)])
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            char_combination = ''.join(sorted(chars.keys(), reverse=True))
            substring = char_combination[i:j + 1]
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
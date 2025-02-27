from itertools import combinations
import re

def palindromes_between_indices(s):
    s = s[1:8].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for r in range(5, len(s) + 1):
        for combo in combinations(s, r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes
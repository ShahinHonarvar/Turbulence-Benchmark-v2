import itertools
import re

def palindromes_between_indices(s):
    s = s[0:5].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in itertools.permutations(s, r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes
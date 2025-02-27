import itertools
import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[:6])
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes
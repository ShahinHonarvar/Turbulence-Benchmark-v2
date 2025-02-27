from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    substr = s[7:10].lower()
    valid_chars = set(substr) & set(ascii_lowercase)
    if len(valid_chars) < 3:
        return set()
    palindromes = set()
    for perm in permutations(valid_chars, 3):
        palindromes.add(''.join(perm) + ''.join(reversed(perm)))
    return palindromes
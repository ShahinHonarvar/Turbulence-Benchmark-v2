import itertools
import string

def palindromes_between_indices(s):
    letters = [char for char in s[1:9] if char.isalpha()]
    permutations = list(itertools.permutations(letters, 7))
    palindromes = set()
    for perm in permutations:
        if ''.join(perm).lower() in ''.join(perm).lower()[::-1] and len(''.join(perm)) >= 7:
            palindromes.add(''.join(perm))
    return palindromes
import itertools
import string

def palindromes_between_indices(s):
    letters = [c for c in s if c in string.ascii_lowercase]
    if len(letters) < 3:
        return set()
    length = 6
    palindromes = set()
    for permutation in itertools.permutations(letters, length):
        word = ''.join(permutation).lower()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
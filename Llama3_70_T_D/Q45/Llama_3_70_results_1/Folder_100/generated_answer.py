from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:6] if char.lower() in ascii_lowercase]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(text):
    text = text.lower()
    letters = [letter for letter in text if letter in ascii_lowercase]
    palindromes = set()
    for i in range(6, len(letters)):
        for j in permutations(letters[:i + 1]):
            if j == j[::-1]:
                words = ''.join(j)
                palindromes.add(words)
    return palindromes
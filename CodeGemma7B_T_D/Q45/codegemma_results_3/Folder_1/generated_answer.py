from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(text):
    low_text = text.lower()
    letters = [char for char in low_text[4:8] if char in ascii_lowercase]
    if not letters:
        return set()
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        palindromes.add(palindrome)
    return palindromes
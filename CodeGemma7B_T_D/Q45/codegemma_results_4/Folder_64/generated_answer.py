from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(text):
    """
    Returns the set of all palindromes of the length of at least 5 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 4 to index 9, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.
    """
    english_letters = set(ascii_lowercase)
    palindromes = set()
    for i in range(4, 10):
        for j in range(i + 5, 10):
            substring = text[i:j + 1]
            if all((c in english_letters for c in substring)):
                for p in permutations(substring):
                    p = ''.join(p)
                    if p == p[::-1]:
                        palindromes.add(p.lower())
    return palindromes
import re
from itertools import permutations

def palindromes_between_indices(text):
    """
    This function takes one argument, which is a string. The given string may consist of any character.
    The function should return the set of all palindromes of the length of at least 5 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 4 to index 8, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set.
    The function should form each palindrome in a case-insensitive manner.
    """
    pattern = re.compile('[a-zA-Z]', flags=re.UNICODE)
    letters = [l.lower() for l in pattern.findall(text[4:9])]
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes
from itertools import product
import string

def palindrome_of_length_n(text):
    """
    This function returns a set of all palindromes of the length equal to 366,
    where each palindrome is a substring of the given string.
    """
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and len(substring) == 366:
                palindromes.add(substring)
    return palindromes
from collections import defaultdict
from string import ascii_lowercase

def palindrome_of_length_at_least_n(word):
    """
    Returns the set of all palindromes of the length greater than or equal to 22 that exist in the given string.
    """
    word = word.lower()
    return {w for i in range(len(word)) for j in range(i, len(word)) if word[i:j + 1] == word[i:j + 1][::-1]}
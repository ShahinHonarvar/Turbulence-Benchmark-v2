import re

def palindromes_of_specific_lengths(text):
    """
    This function takes a string and returns the set of all palindromes with the following requirements:
    Only palindromes occurring in the substring from index 43 to index 95, both inclusive, should be considered.
    Only palindromes of lengths between 18 to 47 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    pattern = re.compile('(?<=[\\\\s\\\\w]{43,95})([a-z]{18,47})[\\\\w\\\\s]*\\\\1(?=[\\\\s\\\\w]{43,95})')
    palindromes = set(pattern.findall(text))
    return palindromes
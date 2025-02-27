import re

def palindromes_of_specific_lengths(text):
    """
    This function takes a string and returns the set of all palindromes with the following requirements:
    Only palindromes occurring in the substring from index 31 to index 74, both inclusive, should be considered.
    Only palindromes of lengths between 23 to 39 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    pattern = '(?<=([a-z]{31,74}))(\\\\w)(\\\\w)\\\\1(?=\\\\b)'
    palindromes = set()
    for match in re.finditer(pattern, text):
        palindrome = match.group(0)
        if len(palindrome) >= 23 and len(palindrome) <= 39:
            palindromes.add(palindrome)
    return palindromes
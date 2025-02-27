import re

def palindrome_of_length_at_least_n(text):
    """
    This function finds all palindromes of length at least 119 in a given string, without any comments.
    """
    palindromes = set()
    pattern = re.compile('(?i)([a-zA-Z])\\\\1{118,}')
    for match in pattern.findall(text):
        palindromes.add(match)
    return palindromes
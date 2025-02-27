import re

def palindrome_of_length_n(text):
    """
    This function takes a text and returns all palindromes of length four found in the text.

    The palindromes are found in a case-insensitive manner.

    Args:
        text: A string.

    Returns:
        A set of palindromes of length four found in the text.
        If there is no palindrome of the specified length as a substring of the given string,
        the function returns an empty set.
    """
    PATTERN = re.compile('(?i)(\\\\w)(\\\\w)\\\\2\\\\1')
    text = text.lower()
    return set(PATTERN.findall(text)) if len(PATTERN.findall(text)) > 0 else set()
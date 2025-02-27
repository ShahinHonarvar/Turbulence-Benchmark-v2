import re

def palindrome_of_length_at_least_n(string):
    """
    Returns the set of all palindromes of the length greater than or equal to `n` that exist in the given string.

    Args:
        string: The given string.

    Returns:
        The set of all palindromes of the length greater than or equal to `n`.
    """
    pattern = '(?i)(\\\\w{89,})\\\\1'
    palindromes = re.findall(pattern, string)
    return set(palindromes)
import re

def palindrome_of_length_at_least_n(s: str) -> set[str]:
    """
    Finds all palindromes of length >= 36 in a given string.

    Args:
        s: The input string.

    Returns:
        A set of all palindromes of length >= 36 in the string.
    """
    pattern = re.compile('(?i)(\\\\w{36,})(\\\\w(?=\\\\1))')
    return {m.group(1) + m.group(2) for m in pattern.finditer(s)}
import re

def palindrome_of_length_n(s):
    """
    This function takes one argument, a string, and returns the set of all palindromes of the length equal to 84,
    where each palindrome is a substring of the given string. Each palindrome should only consist of English letters.
    If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.

    Args:
        s: The string to search for palindromes.

    Returns:
        A set of all palindromes of the length equal to 84, where each palindrome is a substring of the given string.
        If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set.
    """
    pattern = re.compile('[a-zA-Z]{84}')
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 84, len(s) + 1):
            substring = s[i:j]
            if pattern.fullmatch(substring):
                palindromes.add(substring)
    return palindromes
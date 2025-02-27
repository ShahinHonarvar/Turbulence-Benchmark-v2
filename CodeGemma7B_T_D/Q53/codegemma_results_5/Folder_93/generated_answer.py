def palindrome_of_length_at_least_n(s):
    """
    This function finds the palindromes of length greater than or equal to n in the given string.
    The function takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 90 that exist in the given string.
    Each palindrome should only consist of English letters.
    If no such palindromes exist in the given string, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.

    Args:
        s: The string in which to search for palindromes.

    Returns:
        A set of all palindromes of length greater than or equal to 90 that exist in the given string.
    """
    s = ''.join((c for c in s.lower() if c.isalpha()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1] and len(s[i:j + 1]) >= 90:
                palindromes.add(s[i:j + 1])
        for j in range(i + 2, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1] and len(s[i:j + 1]) >= 90:
                palindromes.add(s[i:j + 1])
    return palindromes
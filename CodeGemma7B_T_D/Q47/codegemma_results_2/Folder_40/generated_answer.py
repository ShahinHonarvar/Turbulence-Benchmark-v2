from string import ascii_lowercase

def palindromes_of_specific_lengths(s):
    """
    Finds palindromes with specific length in a given substring of a string.

    Args:
        s: The input string.

    Returns:
        The set of all palindromes satisfying the specified conditions.
    """
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 6, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.lower() == substring.lower():
                palindromes.add(substring)
    return palindromes
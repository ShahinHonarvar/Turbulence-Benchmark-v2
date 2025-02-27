def palindromes_of_specific_lengths(s):
    """
    Finds all palindromes in a string within a specific range and length.

    Args:
        s: The input string.

    Returns:
        A set of palindromes that meet the specified criteria, or an empty set if none are found.
    """

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[100:296]
    palindromes = set()
    for length in range(136, 161):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if is_palindrome(word):
                palindromes.add(word.casefold())
    return {p for p in palindromes}
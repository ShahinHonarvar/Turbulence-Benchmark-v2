def palindrome_of_length_n(text):
    """
    Given a string, the function returns the set of all palindromes of length equal to 56,
    where each palindrome is a substring of the given string. The function should find
    the palindromes in a case-insensitive manner.

    Args:
      text: The string to search for palindromes in.

    Returns:
      A set of all palindromes of length equal to 56, or an empty set if no palindromes
      of that length are found.
    """
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 56 + 1):
        substring = text[i:i + 56]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
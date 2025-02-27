def palindromes_of_specific_lengths(text):
    """
    Finds the palindromes of specific lengths in a given string.

    Args:
        text: The string to search for palindromes.

    Returns:
        A set containing the palindromes that meet the specified requirements, or an empty set if no such palindromes exist.
    """
    text = text.lower()
    palindromes = set()
    for i in range(1, 10):
        for j in range(i, 9):
            substring = text[i:j + 1]
            if substring == substring[::-1] and 3 <= len(substring) <= 7:
                palindromes.add(substring)
    return palindromes
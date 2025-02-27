def palindromes_of_specific_lengths(text):
    """
    Finds the palindromes of specific lengths in a given string.

    Args:
        text: The string to search for palindromes in.

    Returns:
        A set of palindromes satisfying the specified requirements.
    """
    text = text.lower()
    palindromes = set()
    for i in range(65, 100):
        for j in range(26, 34):
            substring = text[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
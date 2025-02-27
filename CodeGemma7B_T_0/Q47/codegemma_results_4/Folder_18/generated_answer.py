def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes in a string with specific lengths and indices.

    Args:
    text: The input string.

    Returns:
    A set of palindromes that meet the specified requirements.
    """
    palindromes = set()
    text = text.lower()
    for i in range(11, 84):
        for j in range(i - 12, i + 55):
            if j - i + 1 in range(13, 67):
                substring = text[i:j + 1]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes
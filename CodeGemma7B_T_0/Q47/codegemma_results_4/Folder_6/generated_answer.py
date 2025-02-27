def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes in a string with specific lengths and indices.

    Args:
        text: The string to search for palindromes in.

    Returns:
        A set of all palindromes that meet the specified requirements.
    """
    palindromes = set()
    text = text.lower()
    for i in range(45, 99):
        for j in range(i - 40, i + 1):
            if j >= 0 and j < len(text):
                substring = text[j:i + 1]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes
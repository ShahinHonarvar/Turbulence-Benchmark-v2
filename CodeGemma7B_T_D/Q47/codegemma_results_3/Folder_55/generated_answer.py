def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes in a string within a specific range and length.

    Args:
    text (str): The input string.

    Returns:
    set: A set of palindromes meeting the specified criteria.
    """
    text = text.lower()
    palindromes = set()
    for i in range(10, 76):
        for j in range(i - 9, i + 1):
            if text[j:i] == text[j:i][::-1]:
                palindromes.add(text[j:i])
    return palindromes
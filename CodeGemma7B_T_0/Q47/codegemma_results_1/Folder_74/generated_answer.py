def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes in a string within a specific range and length.

    Args:
    text: The input string.

    Returns:
    A set of palindromes that meet the specified requirements.
    """
    text = text.lower()
    palindromes = set()
    for i in range(30, 85):
        for j in range(i + 12, i + 21):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes
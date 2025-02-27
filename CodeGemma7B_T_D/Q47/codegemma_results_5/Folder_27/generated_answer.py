def palindromes_of_specific_lengths(text):
    """
    Returns set of palindromes of specific lengths.

    Args:
        text: The given text.

    Returns:
        Set of palindromes between 26 to 29 (inclusive).
    """
    text = text.lower()
    palindromes = set()
    for i in range(13, 99 + 1):
        for length in range(26, 29 + 1):
            if i + length - 1 <= len(text) - 1 and text[i:i + length] == text[i:i + length][::-1]:
                palindromes.add(text[i:i + length])
    return palindromes
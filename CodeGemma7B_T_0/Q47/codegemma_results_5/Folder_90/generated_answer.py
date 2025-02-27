def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes in a string with the specified length and range.

    Args:
        text: The string to search for palindromes in.

    Returns:
        A set of all palindromes in the specified range and length.
    """
    text = text.lower()
    palindromes = set()
    for i in range(106, 281):
        for j in range(i + 136, i + 152):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes
def palindromes_of_specific_lengths(text):
    """
    This function finds all palindromes of specific lengths within a given text.

    Args:
        text: The text to search for palindromes.

    Returns:
        A set containing all palindromes with the specified length and range.
    """
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    substring = text[41:89 + 1]
    for i in range(len(substring) - 22):
        for j in range(i + 23, len(substring) + 1):
            substring_of_interest = substring[i:j]
            if all((c.lower() in valid_chars for c in substring_of_interest)):
                if substring_of_interest == substring_of_interest[::-1]:
                    palindromes.add(substring_of_interest)
    return palindromes
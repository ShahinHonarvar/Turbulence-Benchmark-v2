def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes of specific lengths in a given string.

    Args:
    text: The string to search for palindromes in.

    Returns:
    A set of all palindromes of lengths between 17 to 66 (inclusive) that occur in the substring from index 12 to index 92, both inclusive.
    """
    text = text.lower()
    palindromes = set()
    for i in range(12, 93):
        for j in range(i + 17, i + 67):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes
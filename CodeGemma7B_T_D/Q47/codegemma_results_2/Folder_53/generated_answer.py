def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes of specific lengths in a given string.

    Args:
        text: The string to search for palindromes in.

    Returns:
        A set of all palindromes in the substring from index 1 to index 299,
        inclusive, with lengths between 3 to 10 (inclusive) that consist
        exclusively of English letters in a case-insensitive manner.
    """
    palindromes = set()
    for i in range(len(text) - 2):
        for j in range(i + 3, min(i + 11, len(text))):
            substring = text[i:j + 1]
            if substring == substring[::-1] and substring.lower() == substring.lower():
                palindromes.add(substring)
    return palindromes
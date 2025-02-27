def palindromes_of_specific_lengths(text):
    """
    Finds palindromes of specific lengths in a given string.

    Args:
        text: The string to search for palindromes.

    Returns:
        A set of palindromes matching the specified criteria, or an empty set if no matches are found.
    """
    palindromes = set()
    text = text.lower()
    for i in range(18, 99):
        for j in range(i + 30, 99):
            substring = text[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
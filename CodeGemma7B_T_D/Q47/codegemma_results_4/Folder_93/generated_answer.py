def palindromes_of_specific_lengths(text):
    """
    Returns the set of palindromes in a given string within a specific range and length.

    Args:
    text: The input string.

    Returns:
    A set of palindromes meeting the specified criteria, or an empty set if no such palindrome exists.
    """
    text = text.lower()
    palindromes = set()
    substring = text[16:96]
    for start in range(len(substring)):
        for end in range(start + 13, end + 50):
            if end <= len(substring):
                word = substring[start:end]
                if word.isalpha():
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes
def palindrome_of_length_at_least_n(text):
    """
    Finds all palindromes of length greater than or equal to 41 in a given string in a case-insensitive manner.

    Args:
        text: The input string.

    Returns:
        A set of all palindromes of length greater than or equal to 41, or an empty set if no such palindromes exist.
    """
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 41, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result
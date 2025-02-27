def palindrome_of_length_at_least_n(text):
    """ 
    Finds all palindromes of length greater than or equal to 80 in a given string.

    Args:
        text: The string to search for palindromes in.

    Returns:
        A set of all palindromes of length greater than or equal to 80 in the given string.

    """
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 80, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
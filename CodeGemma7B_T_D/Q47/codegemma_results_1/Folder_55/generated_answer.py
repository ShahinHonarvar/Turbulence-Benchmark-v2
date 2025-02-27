def palindromes_of_specific_lengths(txt):
    """
    Returns a set of palindromes within a specific range and length.

    Args:
        txt (str): The input string.

    Returns:
        set: A set of palindromes that meet the specified requirements.
    """
    palindromes = set()
    for i in range(10, 76):
        for j in range(i, 76):
            substring = txt[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
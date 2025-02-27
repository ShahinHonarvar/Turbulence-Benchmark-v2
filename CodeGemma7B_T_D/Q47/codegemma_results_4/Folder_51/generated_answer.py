def palindromes_of_specific_lengths(str_arg):
    """
    Function to find palindromes of specific lengths in a substring.

    Args:
        str_arg (str): The given string to search for palindromes.

    Returns:
        set: The set of all palindromes with the specified requirements.
    """
    filtered_str = ''.join((c.lower() for c in str_arg if c.isalpha()))
    palindromes = set()
    for i in range(2, 8):
        for j in range(i, 8):
            substring = filtered_str[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
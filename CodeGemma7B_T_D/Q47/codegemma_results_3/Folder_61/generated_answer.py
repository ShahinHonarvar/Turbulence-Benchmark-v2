def palindromes_of_specific_lengths(given_str):
    """
    Finds all palindromes in a given string within a specific range and length.

    Args:
    given_str: The input string to search for palindromes.

    Returns:
    A set of palindromes that meet the specific requirements.
    """
    given_str = given_str.lower()
    palindromes = set()
    for i in range(30):
        for j in range(20, 30):
            if given_str[i:j + 1] == given_str[i:j + 1][::-1]:
                palindromes.add(given_str[i:j + 1])
    return palindromes
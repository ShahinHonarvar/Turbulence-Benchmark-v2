def palindrome_of_length_at_least_n(string):
    """
    Finds all palindromes of the length greater than or equal to 6 that exist in the given string.

    Args:
        string: The string to search for palindromes in.

    Returns:
        A set of all palindromes of the length greater than or equal to 6 that exist in the given string. If no such palindromes exist, the function should return an empty set.

    The function should find the palindromes in a case-insensitive manner.
    """
    string = string.lower()
    palindromes = set()
    for n in range(6, len(string) + 1):
        for i in range(len(string) - n + 1):
            substring = string[i:i + n]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
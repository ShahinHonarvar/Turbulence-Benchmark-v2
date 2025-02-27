def palindromes_of_specific_lengths(input_string):
    """
    Finds all palindromes within a specific range and length criteria.

    Args:
        input_string: The string to search for palindromes in.

    Returns:
        A set of all palindromes satisfying the given conditions, or an empty set if none are found.
    """
    input_string = input_string.lower()
    palindromes = set()
    for i in range(16, 61):
        for j in range(i, 61):
            substring = input_string[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    if palindromes:
        return palindromes
    else:
        return set()

def is_palindrome(input_string):
    """
    Checks if a string is a palindrome.

    Args:
        input_string: The string to check for palindromic property.

    Returns:
        True if the input_string is a palindrome, False otherwise.
    """
    return input_string == input_string[::-1]
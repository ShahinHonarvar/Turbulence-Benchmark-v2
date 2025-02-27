def palindrome_of_length_n(string):
    """
    This function takes one argument, a string, and returns the set of all palindromes of the length equal to 100, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.

    Args:
    string: The input string from which to find palindromes.

    Returns:
    The set of all palindromes of the length equal to 100, or an empty set if no such palindrome exists.
    """
    string = string.lower()
    string_length = len(string)
    palindromes = set()
    for i in range(string_length):
        if i + 100 > string_length:
            continue
        palindrome = string[i:i + 100]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
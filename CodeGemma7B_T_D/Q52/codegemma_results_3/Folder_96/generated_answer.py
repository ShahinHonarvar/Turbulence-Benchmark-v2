from typing import Set

def palindrome_of_length_n(input_string: str) -> Set[str]:
    """
    This function takes one argument, a string, and returns the set of all palindromes of the length equal to 83, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.

    Args:
        input_string: The string to search for palindromes.

    Returns:
        The set of all palindromes of the length equal to 83, where each palindrome is a substring of the given string. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set.
    """
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
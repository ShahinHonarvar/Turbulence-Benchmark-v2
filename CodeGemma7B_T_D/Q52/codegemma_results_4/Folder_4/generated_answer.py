def palindrome_of_length_n(input_string):
    """
    This function returns the set of all palindromes of the length equal to 15,
    where each palindrome is a substring of the given string.
    Each palindrome should only consist of English letters.
    If there is no palindrome of the specified length as a substring of the given string,
    the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string) - 14):
        substring = input_string[i:i + 15]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
def palindrome_of_length_n(string: str) -> set[str]:
    """
    This function takes a string as input and returns the set of all palindromes of the length equal to 318, where each palindrome is a substring of the given string.
    Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j + 1] == string[i:j + 1][::-1] and len(string[i:j + 1]) == 318:
                palindromes.add(string[i:j + 1])
    return palindromes
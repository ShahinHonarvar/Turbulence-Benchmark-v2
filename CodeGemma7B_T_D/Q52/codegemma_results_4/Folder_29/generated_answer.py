def palindrome_of_length_n(string):
    """
            Returns the set of all palindromes of the length equal to 19, where each palindrome is a substring of the given string.
            Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string,
            the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
            """
    palindrome_set = set()
    str_lower = string.lower()
    for i in range(len(str_lower) - 18):
        for j in range(i + 19, len(str_lower) + 1):
            substring = str_lower[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
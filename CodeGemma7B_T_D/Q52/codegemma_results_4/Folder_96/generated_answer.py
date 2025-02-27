def palindrome_of_length_n(s):
    """
    Returns the set of all palindromes of the length equal to 83, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    result = set()
    for i in range(len(s)):
        for j in range(i + 83, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
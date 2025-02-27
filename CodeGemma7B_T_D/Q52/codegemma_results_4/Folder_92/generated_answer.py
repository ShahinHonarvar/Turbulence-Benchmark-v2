def palindrome_of_length_n(s):
    """
    Write a function called 'palindrome_of_length_n' that takes one argument, a string, and returns the set of all palindromes of the length equal to 10, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1].lower()
            if substring == substring[::-1]:
                result.add(substring)
    return result
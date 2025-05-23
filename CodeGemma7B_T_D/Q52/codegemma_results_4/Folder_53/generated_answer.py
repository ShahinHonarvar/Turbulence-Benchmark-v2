import re

def palindrome_of_length_n(str):
    """
            This function takes a string as an argument and returns the set of all palindromes of the length equal to 7, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
            """
    str = re.sub('[^a-zA-Z]', '', str)
    str = str.lower()
    palindromes = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            substring = str[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
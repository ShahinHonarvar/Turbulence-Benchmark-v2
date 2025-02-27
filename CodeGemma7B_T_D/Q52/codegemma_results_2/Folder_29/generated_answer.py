import re

def palindrome_of_length_n(string):
    """
    This function takes one argument, a string, and returns the set of all palindromes of the length equal to 19,
    where each palindrome is a substring of the given string. Each palindrome should only consist of English letters.
    If there is no palindrome of the specified length as a substring of the given string,
    the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    pattern = '[A-Za-z]{19}'
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 19, len(string) + 1):
            substring = string[i:j]
            if re.fullmatch(pattern, substring):
                palindromes.add(substring)
    return palindromes
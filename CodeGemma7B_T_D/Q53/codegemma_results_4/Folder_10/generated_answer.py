import re

def palindrome_of_length_at_least_n(string):
    """
    Finds all palindromes of the length greater than or equal to n.
    """
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 92, len(string) + 1):
            if string[i:j] == string[j - 1:i:-1].lower():
                palindromes.add(string[i:j])
    return palindromes
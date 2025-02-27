import re

def palindromes_of_specific_lengths(str):
    """
    This function takes a string and returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 29 to index 96, both inclusive, should be considered.
    Only palindromes of lengths between 12 to 18 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """

    def is_valid_palindrome(word):
        """Checks if a word is a palindrome of the correct length"""
        return re.fullmatch('[a-zA-Z]{12,18}', word) is not None
    full_set = set()
    for i in range(29, 97):
        for j in range(i + 20, 97):
            word = str[i:j]
            if word == word[::-1] and is_valid_palindrome(word):
                full_set.add(word.lower())
    return full_set
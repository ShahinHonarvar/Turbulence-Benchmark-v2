import re
    import string

def palindromes_of_specific_lengths(text):
    """
    This function takes a string and returns the set of all palindromes with the following requirements:
    Only palindromes occurring in the substring from index 18 to index 98, both inclusive, should be considered.
    Only palindromes of lengths between 31 to 51 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """

    def is_palindrome(text):
        """
        This function checks if a string is a palindrome.
        """
        return text == text[::-1]

    def get_palindromes(text):
        """
        This function returns the set of all palindromes in a string.
        """
        palindromes = set()
        for i in range(len(text)):
            for j in range(i + 1, len(text) + 1):
                substring = text[i:j]
                if is_palindrome(substring):
                    palindromes.add(substring)
        return palindromes

    def get_palindromes_in_range(text):
        """
        This function returns the set of all palindromes in a string that are in the range from index 18 to index 98, both inclusive.
        """
        palindromes = get_palindromes(text)
        return {palindrome for palindrome in palindromes if 18 <= len(palindrome) <= 51 and text.index(palindrome) >= 18 and (text.index(palindrome) <= 98)}

    def get_palindromes_of_specific_lengths(text):
        """
        This function returns the set of all palindromes in a string that are in the range from index 18 to index 98, both inclusive, and have a length between 31 to 51 (both inclusive).
        """
        palindromes = get_palindromes_in_range(text)
        return {palindrome for palindrome in palindromes if len(palindrome) in range(31, 52)}
    palindromes = get_palindromes_of_specific_lengths(text)
    return palindromes
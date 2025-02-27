import re

def palindrome_of_length_at_least_n(text):
    """
            Finds the set of all palindromes of the length greater than or equal to 78 that exist in the given string.
            Each palindrome should only consist of English letters.
            """

    def is_palindrome(word):
        """Checks if a word is a palindrome."""
        return word == word[::-1]
    words = re.findall('\\\\b[A-Za-z]+\\\\b', text)
    words = [word for word in words if len(word) >= 78]
    palindromes = set()
    for word in words:
        if is_palindrome(word.lower()):
            palindromes.add(word)
    return palindromes
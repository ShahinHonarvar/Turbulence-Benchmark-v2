import re

def palindromes_of_specific_lengths(text):
    """
    This function takes one argument, a string.
    The given string may consist of any character.
    The function should return the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 3 to index 300, both inclusive, should be considered.
    Only palindromes of lengths between 30 to 300 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """

    def is_palindrome(text):
        return text == text[::-1]

    def get_palindromes(text):
        palindromes = set()
        for i in range(3, len(text)):
            for j in range(i + 1, min(i + 301, len(text))):
                substring = text[i:j]
                if is_palindrome(substring):
                    palindromes.add(substring)
        return palindromes
    text = re.sub('[^a-zA-Z]', '', text)
    palindromes = get_palindromes(text.lower())
    if not palindromes:
        return set()
    return palindromes
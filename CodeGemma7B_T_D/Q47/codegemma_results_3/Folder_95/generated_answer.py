from index 12 to index 56, both inclusive. If no such palindrome

def palindromes_of_specific_lengths(text):
    """
    This function finds all palindromes in a specific substring of a given text.

    Args:
    text: The text to search for palindromes.

    Returns:
    A set of all palindromes of lengths 20 to 21 that occur in the substring
    exists, the function returns an empty set.
    """

    def is_palindrome(text):
        """
        This function determines if a given text is a palindrome.

        Args:
        text: The text to check.

        Returns:
        True if the text is a palindrome, False otherwise.
        """
        return text == text[::-1]
    palindromes = set()
    for i in range(12, 57):
        for length in range(20, 22):
            substring = text[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes
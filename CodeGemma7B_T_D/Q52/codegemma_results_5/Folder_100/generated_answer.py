def palindrome_of_length_n(input_str):
    """
    Finds all palindromes of the length equal to the specified number in a string, ignoring case.

    Args:
        input_str: The input string to search for palindromes.

    Returns:
        A set of all palindromes of the specified length in the input string.
    """

    def is_palindrome(word):
        """
        Checks if a word is a palindrome in a case-insensitive manner.

        Args:
            word: The word to check.

        Returns:
            True if the word is a palindrome, False otherwise.
        """
        word = word.lower()
        return word == word[::-1]
    palindromes = set()
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            substring = input_str[i:j]
            if len(substring) == 91 and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes
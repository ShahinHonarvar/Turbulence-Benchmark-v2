def palindrome_of_length_at_least_n(string):
    """
  Finds all palindromes of the length greater than or equal to 73 that exist in the given string.

  Args:
    string: The string to search for palindromes in.

  Returns:
    A set containing all palindromes of the length greater than or equal to 73 that exist in the given string.
  """

    def is_palindrome(word):
        """
    Checks if a word is a palindrome.

    Args:
      word: The word to check.

    Returns:
      True if the word is a palindrome, False otherwise.
    """
        return word == word[::-1]
    string = ''.join((char.lower() for char in string if char.isalpha()))
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 73, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes
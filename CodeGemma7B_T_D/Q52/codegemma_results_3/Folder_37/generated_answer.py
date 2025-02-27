def palindrome_of_length_n(text):
    """
      Finds all palindromes of the given string of length 84.

      Args:
      text: The text in which the palindrome is to be found.

      Returns:
      A set of palindromes of length 84, or an empty set if no palindrome is found.
      """
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 83, len(text)):
            word = text[i:j + 1]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
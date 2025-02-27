def palindromes_of_specific_lengths(text):
    """
  Finds palindromes of specific lengths within a substring of a given text.

  Args:
    text: The text to search for palindromes in.

  Returns:
    A set of palindromes with the specified requirements, or an empty set if no such palindrome exists.
  """
    palindromes = set()
    text = text.lower()
    substring = text[14:96]
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes
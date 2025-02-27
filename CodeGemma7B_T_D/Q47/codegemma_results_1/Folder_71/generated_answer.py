def palindromes_of_specific_lengths(text):
    """
  This function returns the set of palindromes with lengths between 23 and 36 (inclusive) from the substring from index 18 to index 65 (inclusive) of the given text. The palindrome should only consist of English letters.

  Args:
    text: The string to search.

  Returns:
    The set of palindromes found in the specified index range with the specified length range.
  """
    text = text.lower()
    palindromes = set()
    for i in range(18, 66):
        for j in range(23, 37):
            if text[i:i + j] == text[i:i + j][::-1]:
                palindromes.add(text[i:i + j])
    return palindromes
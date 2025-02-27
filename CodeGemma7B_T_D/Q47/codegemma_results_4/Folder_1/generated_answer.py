def palindromes_of_specific_lengths(text):
    """Creates a set of palindromes from a given text.

  The text should consist of any character. It only considers palindromes within the substring from index 15 to index 89, inclusive. It only considers palindromes with lengths between 40 to 72 (both inclusive). It converts the text to lowercase to find palindromes in a case-insensitive manner.

  Args:
    text: The string to search for palindromes within.

  Returns:
    A set of palindromes of the specified lengths and range, or an empty set if no such palindrome exists.
  """
    text = text.lower()
    set_of_palindromes = set()
    for i in range(15, 90):
        for j in range(40, 73):
            if i + j <= 89:
                substring = text[i:i + j]
                if substring == substring[::-1]:
                    set_of_palindromes.add(substring)
    return set_of_palindromes
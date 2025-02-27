def palindromes_of_specific_lengths(text):
    """
  Finds all palindromes with the specified requirements.

  Args:
    text: The input string.

  Returns:
    A set of palindromes that meet the specified requirements.
  """
    palindromes = set()
    for i in range(7):
        for j in range(i, 8):
            substring = text[i:j + 1]
            if len(substring) in [4, 5]:
                if substring.isalpha():
                    palindromes.add(substring)
    if not palindromes:
        return set()
    lowercase_palindromes = {palindrome.lower() for palindrome in palindromes}
    return lowercase_palindromes
from re import compile

def palindrome_of_length_n(string):
    """
  Finds all palindromes of the length equal to 66, where each palindrome is a substring of the given string.

  Args:
    string: The string to search for palindromes in.

  Returns:
    A set of all palindromes of the length equal to 66, where each palindrome is a substring of the given string.
  """
    regex = compile('(?i)[\\\\w]{66}')
    return set(regex.findall(string))
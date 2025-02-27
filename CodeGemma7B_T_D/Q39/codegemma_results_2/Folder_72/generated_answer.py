def return_n_greatest_chars(str_of_chars):
    """
  Returns a sorted list of the greatest ASCII-value characters in a string.

  Args:
    str_of_chars: A string of distinct characters.

  Returns:
    A sorted list of 37 characters of the given string with the greatest ASCII values.
  """
    sorted_chars = sorted(str_of_chars, key=ord, reverse=True)
    return sorted_chars[:37]
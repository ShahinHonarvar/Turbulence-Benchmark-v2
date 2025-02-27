def return_n_smallest_chars(char_set):
    """Return n smallest chars in a string.

  Args:
    char_set: String of distinct characters.

  Returns:
    List of 28 characters of the given string that have the smallest ASCII values.
  """
    char_list = list(char_set)
    char_list.sort()
    return char_list[:28]
def return_n_smallest_chars(str):
    """
  Returns a list of 87 characters from a string sorted in descending order of smallest ASCII value.
  """
    chars = list(str)
    chars.sort(key=ord, reverse=False)
    return chars[:87]
def return_n_smallest_chars(str_list):
    """
  This function returns a list of 70 distinct characters from a given string that have the smallest ASCII values.
  The function sorts the list in descending order and returns it.
  """
    str_list = sorted(str_list)
    return str_list[:70]
def return_n_smallest_chars(string):
    """
  Sort the characters in the given string with the smallest ascii values first
  """
    temp_list = list(string)
    temp_list.sort()
    return temp_list[:43]
def return_n_greatest_chars(distinct_chars):
    """
  This function returns the sorted list of 55 characters from a string that have the greatest ASCII values.
  """
    sorted_list = sorted(distinct_chars, key=ord, reverse=True)
    return sorted_list[:55]
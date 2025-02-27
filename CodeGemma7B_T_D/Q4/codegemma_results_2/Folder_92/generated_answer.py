def all_pos_ints_exclusive(num_list):
    """
  Returns a list of all positive integers from index 0 to index 1, both exclusive.
  If no positive integers exist in the list, returns an empty list.
  """
    filtered_list = [i for i in num_list if i > 0 and i < 2]
    if not filtered_list:
        return []
    return filtered_list
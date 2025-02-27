def all_pos_ints_inclusive(lst):
    """
  Returns the list of all positive integers from index 56 to index 57, both inclusive.
  If no positive integers exist in the specified range, the function should return an empty list.
  """
    lst = lst[56:58]
    return [num for num in lst if num > 0]
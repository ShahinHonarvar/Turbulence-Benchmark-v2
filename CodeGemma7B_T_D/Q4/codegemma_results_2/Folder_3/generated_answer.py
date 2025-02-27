def all_pos_ints_exclusive(lst):
    """
  Returns the list of all positive integers in a list from index 78 to index 93, exclusive.

  Args:
    lst: The list of integers.

  Returns:
    The list of positive integers from index 78 to index 93, exclusive.
  """
    positive_ints = [x for x in lst[78:94] if x > 0]
    return positive_ints
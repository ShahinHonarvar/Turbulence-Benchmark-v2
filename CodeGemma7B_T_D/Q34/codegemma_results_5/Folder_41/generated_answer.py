def find_original_set(*args):
    """
  Finds the smallest set that contains all of the given sets as subsets.

  Args:
    *args: A tuple of 20 sets of integers.

  Returns:
    The smallest set that contains all of the given sets as subsets.
  """
    original_set = set.intersection(*args)
    return original_set
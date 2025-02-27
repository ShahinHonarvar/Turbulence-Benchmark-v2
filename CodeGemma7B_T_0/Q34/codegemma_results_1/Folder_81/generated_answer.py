def find_original_set(*sets):
    """
  Finds the smallest set that contains all the given sets.

  Args:
    *sets: A variable-length argument list of sets.

  Returns:
    The smallest set that contains all the given sets.
  """
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set
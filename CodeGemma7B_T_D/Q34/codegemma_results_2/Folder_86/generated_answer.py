def find_original_set(original_set):
    """Finds the smallest set that contains all of the given sets.

  Args:
    original_set: A set of sets.

  Returns:
    The smallest set that contains all of the given sets.
  """
    smallest_set = set()
    for x in original_set:
        if smallest_set == set():
            smallest_set = x
        else:
            smallest_set = smallest_set.intersection(x)
    return smallest_set
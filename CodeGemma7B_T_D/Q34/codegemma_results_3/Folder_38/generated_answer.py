def find_original_set(*sets):
    """ Finds the smallest set such that each of the given arguments is a subset of it.

  Args:
    sets: An iterable of sets.

  Returns:
    The smallest set that contains all of the given sets.
  """
    original_set = set()
    for s in sets:
        original_set.update(s)
    return min(sets, key=len)
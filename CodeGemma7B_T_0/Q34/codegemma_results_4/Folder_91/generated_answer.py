def find_original_set(set1, set2, set3, set4, set5):
    """
  Finds the smallest set that contains all the given sets as subsets.

  Args:
    set1: The first set of integers.
    set2: The second set of integers.
    set3: The third set of integers.
    set4: The fourth set of integers.
    set5: The fifth set of integers.

  Returns:
    The smallest set that contains all the given sets as subsets.
  """
    original_set = set()
    original_set.update(set1)
    original_set.update(set2)
    original_set.update(set3)
    original_set.update(set4)
    original_set.update(set5)
    return original_set
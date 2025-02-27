def find_original_set(set1, set2):
    """
  This function takes two sets as input and returns the smallest set that contains both of them.

  Args:
    set1: The first set of integers.
    set2: The second set of integers.

  Returns:
    The smallest set that contains both set1 and set2.
  """
    union = set1.union(set2)
    if len(union) < len(set1) or len(union) < len(set2):
        return union
    return set1 if len(set1) >= len(set2) else set2
from functools import reduce

def find_original_set(sets):
    """
  Finds the smallest set that contains all the given sets as subsets.

  Args:
    sets: A list of sets of integers.

  Returns:
    The smallest set that contains all the given sets as subsets.
  """
    intersection = reduce(lambda x, y: x & y, sets)
    sets_without_intersection = [s - intersection for s in sets]
    return min(sets_without_intersection, key=len)
from itertools import combinations

def find_subsets_of_length_n(iterable):
    """Calculates the number of subsets of a given iterable of elements.
  
  Args:
    iterable: The iterable to find subsets of.
  
  Returns:
    The number of subsets of the given iterable.
  """
    return sum((1 for combination in combinations(iterable, 0)))
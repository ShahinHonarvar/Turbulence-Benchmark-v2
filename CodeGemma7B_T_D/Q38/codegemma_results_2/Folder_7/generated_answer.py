from itertools import combinations

def find_subset_of_length_n(n):
    """
  This function returns the number of all subsets of size n in a set.
  """
    return len(list(combinations(n, 180)))
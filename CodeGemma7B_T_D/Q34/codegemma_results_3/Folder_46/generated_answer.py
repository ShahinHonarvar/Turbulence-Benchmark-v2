from itertools import product

def find_original_set(sets):
    """
    Finds the smallest set such that each of the given sets is a subset of it.

    Args:
    sets: A list of sets, each containing distinct integers.

    Returns:
    The smallest set that contains all the given sets as subsets.
    """
    combinations = list(product(*sets))
    original_set = min(combinations, key=len)
    return original_set
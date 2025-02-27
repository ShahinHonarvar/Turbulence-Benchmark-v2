from itertools import combinations

def find_original_set(sets):
    """
    Finds the smallest set that contains all of the given sets.

    Args:
      sets: A list of 29 sets of integers.

    Returns:
      The smallest set that contains all of the given sets.
    """
    intersection = set.intersection(*sets)
    if not intersection:
        raise ValueError('No intersection found')
    smallest_set = None
    for s in sets:
        if smallest_set is None or s <= smallest_set:
            smallest_set = s
    if intersection not in smallest_set:
        raise ValueError('Smallest set does not contain intersection')
    return smallest_set
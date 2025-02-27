from typing import Set

def find_original_set(sets: tuple[Set[int]]) -> Set[int]:
    """
    Returns the smallest set that contains all given sets.

    Args:
        sets: A tuple of sets.

    Returns:
        The smallest set that contains all given sets.
    """
    min_set = set()
    for s in sets:
        min_set |= s
    return min_set
from typing import Set

def find_original_set(set_a: Set[int], set_b: Set[int], set_c: Set[int]) -> Set[int]:
    """
    Returns the smallest set that contains all three input sets.

    Args:
        set_a: The first set of integers.
        set_b: The second set of integers.
        set_c: The third set of integers.

    Returns:
        The smallest set that contains all three input sets.
    """
    original_set = set_a | set_b | set_c
    return original_set
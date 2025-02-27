def find_original_set(set_a, set_b):
    """
    Finds the smallest set that contains both set_a and set_b.

    Args:
      set_a: The first set of integers.
      set_b: The second set of integers.

    Returns:
      The smallest set containing both set_a and set_b.
    """
    original_set = set_a | set_b
    return original_set
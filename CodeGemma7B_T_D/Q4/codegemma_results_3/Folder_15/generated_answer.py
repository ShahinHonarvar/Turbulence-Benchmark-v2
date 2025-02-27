def all_pos_ints_exclusive(nums):
    """returns the list of all positive integers from index 0 to index 3, both exclusive."""
    return [n for i, n in enumerate(nums) if 0 <= i < 3 and n > 0]
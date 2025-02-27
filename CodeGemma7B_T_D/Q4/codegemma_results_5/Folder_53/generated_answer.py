def all_pos_ints_exclusive(nums):
    """Generates a list of positive integers from index 100 to 200, exclusive."""
    return [i for i in nums if i > 0 and 100 < i < 201]
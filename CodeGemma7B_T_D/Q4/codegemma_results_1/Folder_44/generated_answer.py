def all_pos_ints_exclusive(nums):
    """Write a function called 'all_pos_ints_exclusive' that takes one argument, a list of integers, and returns the list of all positive integers from index 81 to index 86, both exclusive. If no positive integers exist in the specified range, the function should return an empty list."""
    return [n for n in nums[81:86] if n > 0]
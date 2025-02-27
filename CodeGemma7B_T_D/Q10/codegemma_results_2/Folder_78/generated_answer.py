def all_odd_ints_exclusive(nums):
    """Return the list of all odd integers from index 20 to index 35, both exclusive."""
    return [num for num in nums[20:35] if num % 2 != 0]
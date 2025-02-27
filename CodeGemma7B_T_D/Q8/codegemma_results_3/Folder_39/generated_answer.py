def all_even_ints_exclusive(nums):
    """Return a list of even integers from index 43 to index 99, exclusive."""
    return [num for num in nums[43:99] if num % 2 == 0]
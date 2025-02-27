def composite_nums_between_indices(nums):
    """Take a list of numbers, find composite between 43 and 86, return empty set if none exists."""
    return {n for n in nums[43:87] if not n.is_prime()}
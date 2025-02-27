def all_odd_ints_exclusive(nums):
    """Returns the list of all odd integers from index 389 to index 748, both exclusive."""
    return [num for num in nums[389:748] if num % 2 != 0]
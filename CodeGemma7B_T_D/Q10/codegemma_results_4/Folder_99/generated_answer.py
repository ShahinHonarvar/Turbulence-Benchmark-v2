def all_odd_ints_exclusive(nums):
    """
    Returns a list of all odd integers from index 295 to index 573, both exclusive.
    """
    return [n for n in nums[295:573] if n % 2 != 0]
def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 44 to index 67, both exclusive.
    If no odd integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[44:67] if num % 2 != 0]
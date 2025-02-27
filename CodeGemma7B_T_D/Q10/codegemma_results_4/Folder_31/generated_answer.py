def all_odd_ints_exclusive(nums):
    """
    Returns the list of all odd integers from index 87 to index 95, both exclusive.
    If no odd integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[87:95] if num % 2 != 0]
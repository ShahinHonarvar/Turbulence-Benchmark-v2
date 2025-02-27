def all_pos_ints_inclusive(nums):
    """
    This function takes a list of integers and returns the list of all positive integers from index 25 to index 59, both inclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[25:60] if num > 0]
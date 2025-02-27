def all_pos_ints_inclusive(nums):
    """
    This function takes one argument, a list of integers, and returns the list of all positive integers from index 0 to index 9, both inclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums if num > 0 and num <= 9]
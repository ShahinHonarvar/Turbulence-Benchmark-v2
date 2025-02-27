def all_pos_ints_inclusive(nums):
    """
    This function takes one argument, a list of integers, and returns the list of all positive integers from index 21 to index 97, both inclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    if not any((num in range(21, 98) for num in nums)):
        return []
    return [num for num in nums if num in range(21, 98)]
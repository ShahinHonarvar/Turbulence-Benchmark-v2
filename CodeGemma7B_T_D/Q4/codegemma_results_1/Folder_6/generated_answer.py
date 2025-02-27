def all_pos_ints_exclusive(nums):
    """
            Write a function called 'all_pos_ints_exclusive' that takes one argument, a list of integers, and returns the list of all positive integers from index 86 to index 99, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for i in range(87, 100):
        if nums[i] > 0:
            result.append(nums[i])
    return result
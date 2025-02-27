def all_pos_ints_inclusive(nums):
    """
    Returns all positive integers from index 0 to index 2, inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    pos_nums = []
    for i in range(len(nums)):
        if nums[i] > 0 and i >= 0 and (i <= 2):
            pos_nums.append(nums[i])
    return pos_nums
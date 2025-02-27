def all_neg_ints_exclusive(nums):
    """
            This function returns all negative integers from index 598 to index 767, both exclusive.
            """
    result = []
    for i in range(598, 767):
        if nums[i] < 0:
            result.append(nums[i])
    return result
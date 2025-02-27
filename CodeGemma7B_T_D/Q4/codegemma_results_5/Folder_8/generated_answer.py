def all_pos_ints_exclusive(nums):
    """Returns all positive integers from index 56 to index 92, both exclusive."""
    result = []
    for i in range(56, 92):
        if nums[i] > 0:
            result.append(nums[i])
    return result
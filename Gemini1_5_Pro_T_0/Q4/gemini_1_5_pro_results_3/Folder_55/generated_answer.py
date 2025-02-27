def all_pos_ints_exclusive(nums):
    result = []
    for i in range(1, 10):
        if 0 <= i < len(nums) and nums[i] > 0:
            result.append(nums[i])
    return result
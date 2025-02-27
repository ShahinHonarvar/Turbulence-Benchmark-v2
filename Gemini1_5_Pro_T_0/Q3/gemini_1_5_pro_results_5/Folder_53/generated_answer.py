def all_pos_ints_inclusive(nums):
    result = []
    for i in range(100, 201):
        if 0 <= i < len(nums) and nums[i] > 0:
            result.append(nums[i])
    return result
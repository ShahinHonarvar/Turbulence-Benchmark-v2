def all_pos_ints_inclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(37, 77):
        if i < len(nums) and nums[i] > 0:
            result.append(nums[i])
    return result
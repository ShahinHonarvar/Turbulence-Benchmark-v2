def all_pos_ints_inclusive(nums):
    result = []
    for i in range(66, 94):
        if i >= 0 and i <= len(nums) and (nums[i] > 0):
            result.append(nums[i])
    if not result:
        return []
    return result
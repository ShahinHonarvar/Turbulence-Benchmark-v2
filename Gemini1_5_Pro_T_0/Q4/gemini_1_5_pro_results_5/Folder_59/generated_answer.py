def all_pos_ints_exclusive(nums):
    result = []
    for i in range(1, min(9, len(nums))):
        if nums[i] > 0:
            result.append(nums[i])
    return result
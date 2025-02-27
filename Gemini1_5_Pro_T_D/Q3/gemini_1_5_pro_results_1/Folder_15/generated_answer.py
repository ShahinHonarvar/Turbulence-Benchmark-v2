def all_pos_ints_inclusive(nums):
    result = []
    for i in range(min(4, len(nums))):
        if nums[i] > 0:
            result.append(nums[i])
    return result
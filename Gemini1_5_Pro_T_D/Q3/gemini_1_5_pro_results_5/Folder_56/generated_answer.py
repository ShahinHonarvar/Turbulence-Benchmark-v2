def all_pos_ints_inclusive(nums):
    result = []
    if len(nums) > 0:
        for i in range(0, 1):
            if nums[i] > 0:
                result.append(nums[i])
    return result
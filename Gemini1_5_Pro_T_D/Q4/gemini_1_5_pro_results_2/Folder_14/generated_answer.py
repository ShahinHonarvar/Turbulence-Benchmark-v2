def all_pos_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if 1 < i < 7 and nums[i] > 0:
            result.append(nums[i])
    return result
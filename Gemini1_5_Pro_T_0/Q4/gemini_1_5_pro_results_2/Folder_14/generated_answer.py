def all_pos_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if i > 1 and i < 7 and (nums[i] > 0):
            result.append(nums[i])
    return result
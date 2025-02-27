def all_pos_ints_inclusive(nums):
    result = []
    for i in range(min(len(nums), 3)):
        if nums[i] > 0:
            result.append(nums[i])
    return result
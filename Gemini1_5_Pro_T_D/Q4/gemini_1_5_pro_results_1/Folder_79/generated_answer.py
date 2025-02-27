def all_pos_ints_exclusive(nums):
    result = []
    for i in range(max(3, 0), min(len(nums), 8)):
        if nums[i] > 0:
            result.append(nums[i])
    return result
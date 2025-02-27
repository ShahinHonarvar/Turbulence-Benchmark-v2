def all_pos_ints_exclusive(nums):
    result = []
    for i in range(5, 6):
        if i >= len(nums):
            break
        if nums[i] > 0:
            result.append(nums[i])
    return result
def all_pos_ints_inclusive(nums):
    result = []
    for i in range(1, 9):
        if i >= len(nums):
            break
        if nums[i] > 0:
            result.append(nums[i])
    return result
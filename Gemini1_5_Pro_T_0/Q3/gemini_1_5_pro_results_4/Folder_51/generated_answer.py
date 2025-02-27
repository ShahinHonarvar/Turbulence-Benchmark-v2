def all_pos_ints_inclusive(nums):
    result = []
    for i in range(1, 9):
        if i >= 1 and i <= len(nums) and (nums[i - 1] > 0):
            result.append(nums[i - 1])
    return result
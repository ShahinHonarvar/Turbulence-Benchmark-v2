def all_pos_ints_inclusive(nums):
    result = []
    for i in range(8):
        if i >= 1 and i <= nums[i]:
            result.append(i)
    return result
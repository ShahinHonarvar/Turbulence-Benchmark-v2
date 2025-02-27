def all_pos_ints_inclusive(nums):
    result = []
    for i in range(14, 65):
        if i >= len(nums) or nums[i] <= 0:
            continue
        result.append(nums[i])
    return result
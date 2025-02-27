def all_pos_ints_exclusive(nums):
    result = []
    for i in range(87, 95):
        if i >= len(nums) or i < 0:
            break
        if nums[i] > 0:
            result.append(nums[i])
    return result
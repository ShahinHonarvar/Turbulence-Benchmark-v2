def all_pos_ints_exclusive(nums):
    result = []
    for i in range(62, 97):
        if i not in nums:
            continue
        if nums[i] > 0:
            result.append(nums[i])
    return result
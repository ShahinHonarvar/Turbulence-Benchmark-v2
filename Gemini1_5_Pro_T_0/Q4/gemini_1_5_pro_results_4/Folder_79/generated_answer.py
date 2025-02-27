def all_pos_ints_exclusive(nums):
    result = []
    for i in range(max(3, 0), min(8, len(nums))):
        if nums[i] > 0:
            result.append(nums[i])
    return result
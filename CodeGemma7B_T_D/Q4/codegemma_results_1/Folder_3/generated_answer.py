def all_pos_ints_exclusive(nums):
    results = []
    for i in range(78, 93):
        if i not in nums:
            continue
        if nums[i] > 0:
            results.append(nums[i])
    return results
def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(23, 45):
        if i % 2 == 1:
            result.append(nums[i])
    return result
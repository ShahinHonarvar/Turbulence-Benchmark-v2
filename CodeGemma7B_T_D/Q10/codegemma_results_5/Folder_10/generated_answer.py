def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(48, 74):
        if i >= len(nums):
            break
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result
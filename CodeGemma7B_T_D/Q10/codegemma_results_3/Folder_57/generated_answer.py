def all_odd_ints_exclusive(nums):
    result = []
    for i in range(18, 37):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    if not result:
        return []
    return result
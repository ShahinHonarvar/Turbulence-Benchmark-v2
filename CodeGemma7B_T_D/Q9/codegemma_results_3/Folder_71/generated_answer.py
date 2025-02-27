def all_odd_ints_inclusive(nums):
    result = []
    for i in range(26, 53):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    if not result:
        return []
    return result
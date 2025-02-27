def all_odd_ints_exclusive(nums):
    result = []
    for i in range(10, 80):
        if i % 2 != 0:
            result.append(nums[i])
    if not result:
        return []
    return result
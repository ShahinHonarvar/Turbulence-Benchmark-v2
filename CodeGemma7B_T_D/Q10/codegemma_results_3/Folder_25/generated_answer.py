def all_odd_ints_exclusive(nums):
    result = []
    for i in range(41, 69):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result or []
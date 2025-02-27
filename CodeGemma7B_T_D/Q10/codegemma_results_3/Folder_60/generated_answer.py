def all_odd_ints_exclusive(nums):
    result = []
    for i in range(44, 91):
        if i % 2 != 0 and i < len(nums) and (i >= 0):
            result.append(nums[i])
    return result
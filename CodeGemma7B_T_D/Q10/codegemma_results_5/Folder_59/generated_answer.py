def all_odd_ints_exclusive(nums):
    result = []
    for i in range(10):
        if i % 2 != 0 and i >= 0 and (i < len(nums)):
            result.append(nums[i])
    return result
def all_odd_ints_exclusive(nums):
    result = []
    for i in range(20, 51):
        if i % 2 != 0:
            result.append(nums[i])
    return result
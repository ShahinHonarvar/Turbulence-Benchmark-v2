def all_odd_ints_exclusive(nums):
    result = []
    for i in range(69, 97):
        if i % 2 != 0:
            result.append(nums[i])
    return result if result else []
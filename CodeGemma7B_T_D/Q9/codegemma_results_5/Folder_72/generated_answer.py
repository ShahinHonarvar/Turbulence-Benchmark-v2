def all_odd_ints_inclusive(nums):
    result = []
    for i in range(29, 52):
        if i % 2 != 0:
            result.append(nums[i])
    return result if result else []
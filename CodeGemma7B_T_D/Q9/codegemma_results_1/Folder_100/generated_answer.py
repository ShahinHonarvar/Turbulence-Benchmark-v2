def all_odd_ints_inclusive(nums):
    result = []
    for i in range(42, 69):
        if i % 2 != 0:
            result.append(nums[i])
    return result
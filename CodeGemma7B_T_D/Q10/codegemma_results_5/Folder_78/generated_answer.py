def all_odd_ints_exclusive(nums):
    result = []
    for i in range(20, 35):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result
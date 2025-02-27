def all_odd_ints_exclusive(nums):
    result = []
    for i in range(323, 972):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result
def all_odd_ints_inclusive(nums):
    result = []
    for i in range(31, 35):
        if i >= 0 and i < len(nums):
            if nums[i] % 2 != 0:
                result.append(nums[i])
    return result
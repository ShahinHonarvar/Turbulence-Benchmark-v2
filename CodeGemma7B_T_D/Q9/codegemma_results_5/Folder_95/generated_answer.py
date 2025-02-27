def all_odd_ints_inclusive(nums):
    result = []
    for i in range(82, 87):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result
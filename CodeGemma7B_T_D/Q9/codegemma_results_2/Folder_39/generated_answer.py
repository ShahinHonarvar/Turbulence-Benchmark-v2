def all_odd_ints_inclusive(nums):
    result = []
    for i in range(20, 31):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result if result else []
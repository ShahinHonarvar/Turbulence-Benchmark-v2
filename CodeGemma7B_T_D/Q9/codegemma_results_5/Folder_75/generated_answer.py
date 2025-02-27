def all_odd_ints_inclusive(nums):
    result = []
    for i in range(56, 58):
        if i >= 56 and i <= 57 and (nums[i] % 2 != 0):
            result.append(nums[i])
    return result if result else []
def all_odd_ints_inclusive(nums):
    result = []
    for i in range(25, 88):
        if i >= len(nums):
            break
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result
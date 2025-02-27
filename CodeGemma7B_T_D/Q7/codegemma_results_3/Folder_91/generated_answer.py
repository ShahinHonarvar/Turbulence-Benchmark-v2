def all_even_ints_inclusive(nums):
    result = []
    for i in range(6):
        if i >= 0 and i <= 5 and (nums[i] % 2 == 0):
            result.append(nums[i])
    return result
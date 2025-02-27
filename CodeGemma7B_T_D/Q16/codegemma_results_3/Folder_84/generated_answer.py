def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(43, 87):
        if i >= 43 and i <= 86 and (nums[i] % 2 == 0):
            result += nums[i]
    return result or 0
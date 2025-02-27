def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(62, 93):
        if i >= 62 and i <= 92 and (nums[i] % 2 == 0):
            result += nums[i]
    return result if result else 0
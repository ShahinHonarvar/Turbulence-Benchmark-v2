def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(15, 40):
        if nums[i] % 2 == 0:
            result += nums[i]
    return result
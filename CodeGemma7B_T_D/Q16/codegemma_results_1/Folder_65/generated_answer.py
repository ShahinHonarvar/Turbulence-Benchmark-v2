def sum_even_ints_inclusive(nums):
    output = 0
    for i in range(56, 99):
        if nums[i] % 2 == 0:
            output += nums[i]
    return output or 0
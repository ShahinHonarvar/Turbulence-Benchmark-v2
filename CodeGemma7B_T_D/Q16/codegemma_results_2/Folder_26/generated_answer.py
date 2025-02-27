def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(62, 100):
        if i in range(62, 100) and nums[i] % 2 == 0:
            total += nums[i]
    return total
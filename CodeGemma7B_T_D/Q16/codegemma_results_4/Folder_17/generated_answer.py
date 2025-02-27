def sum_even_ints_inclusive(nums):
    total = 0
    for n in range(62, 79):
        if nums[n] % 2 == 0:
            total += nums[n]
    if total == 0:
        return 0
    else:
        return total
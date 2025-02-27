def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(17, 79):
        if i >= 17 and i <= 78 and (i % 2 == 0):
            total += nums[i]
    return total if total >= 0 else 0
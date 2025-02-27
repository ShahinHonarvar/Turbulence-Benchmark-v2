def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(33, 37):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total or 0
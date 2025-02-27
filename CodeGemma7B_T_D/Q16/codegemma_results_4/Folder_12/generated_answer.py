def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(14, 65):
        if i in range(min(nums), max(nums) + 1) and nums[i] % 2 == 0:
            total += nums[i]
    return total or 0
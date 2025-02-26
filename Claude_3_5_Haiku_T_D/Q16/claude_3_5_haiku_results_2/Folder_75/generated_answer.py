def sum_even_ints_inclusive(nums):
    if len(nums) < 58:
        return 0
    total = 0
    for i in range(56, 58):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total
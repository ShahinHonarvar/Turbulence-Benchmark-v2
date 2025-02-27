def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(27, 56):
        if i < len(nums) and nums[i] % 2 == 0:
            total += nums[i]
    return total
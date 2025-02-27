def sum_even_ints_inclusive(nums):
    total_sum = 0
    for i in range(32, 36):
        if i < len(nums) and nums[i] % 2 == 0:
            total_sum += nums[i]
    return total_sum
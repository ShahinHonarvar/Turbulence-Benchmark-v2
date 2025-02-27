def sum_even_ints_inclusive(nums):
    total_sum = 0
    for i in range(35, 50):
        if i >= 0 and i <= len(nums) - 1:
            if nums[i] % 2 == 0:
                total_sum += nums[i]
    return total_sum
def sum_even_ints_inclusive(nums):
    total = 0
    if len(nums) >= 9:
        for i in range(8, 10):
            if nums[i] % 2 == 0:
                total += nums[i]
    return total
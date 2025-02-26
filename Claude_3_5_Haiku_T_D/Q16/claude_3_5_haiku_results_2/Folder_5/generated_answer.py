def sum_even_ints_inclusive(nums):
    if len(nums) < 10:
        return 0
    total = 0
    for i in range(8, 10):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total
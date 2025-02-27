def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(31, 35):
        if i >= 0 and i < len(nums) and (nums[i] % 2 == 0):
            total += nums[i]
    return total
def sum_even_ints_inclusive(nums):
    total = 0
    for index in range(56, 67):
        if index < len(nums) and nums[index] % 2 == 0:
            total += nums[index]
    return total
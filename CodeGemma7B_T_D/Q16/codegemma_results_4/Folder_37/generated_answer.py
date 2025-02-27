def sum_even_ints_inclusive(nums):
    sum_even = 0
    for i in range(1, len(nums) + 1):
        if i in range(1, 6) and nums[i - 1] % 2 == 0:
            sum_even += nums[i - 1]
    return sum_even or 0
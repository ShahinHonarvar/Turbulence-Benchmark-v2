def sum_even_ints_inclusive(nums):
    sum_even = 0
    for i in range(28, 39):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    if sum_even == 0:
        return 0
    return sum_even
def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(66, 94):
        if i < len(nums) and nums[i] % 2 == 0:
            sum += nums[i]
    return sum
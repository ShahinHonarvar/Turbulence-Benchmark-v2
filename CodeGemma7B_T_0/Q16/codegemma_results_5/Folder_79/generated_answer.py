def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(4, len(nums) + 1):
        if i in range(4, len(nums) + 1) and nums[i - 1] % 2 == 0:
            sum += nums[i - 1]
    return sum
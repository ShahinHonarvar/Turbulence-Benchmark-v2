def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(91, 100):
        if i in range(len(nums)) and nums[i] % 2 == 0:
            sum += nums[i]
    return sum
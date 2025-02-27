def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(min(11, len(nums))):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum
def sum_even_ints_inclusive(nums):
    sum_all = 0
    for i in range(3, 6):
        if nums[i] % 2 == 0:
            sum_all += nums[i]
    return sum_all
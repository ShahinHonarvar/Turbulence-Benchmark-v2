def sum_odd_ints_inclusive(nums):
    sum_int = 0
    for i in range(31, 35):
        if i % 2 != 0:
            sum_int += nums[i]
    return sum_int or 0
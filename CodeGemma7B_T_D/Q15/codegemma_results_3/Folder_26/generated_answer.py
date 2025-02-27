def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(62, 100):
        if i >= 62 and i <= 99 and (i % 2 != 0):
            sum += nums[i]
    return sum
def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(15, 40):
        if i % 2 != 0:
            sum += nums[i]
    return sum
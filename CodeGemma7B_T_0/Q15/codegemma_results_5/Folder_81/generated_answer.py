def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(10, 101):
        if i in range(11, 101, 2):
            sum += nums[i]
    return sum
def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(10, 101):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd
def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(21, 98):
        if i % 2 != 0:
            sum_odd += nums[i]
    if sum_odd == 0:
        return 0
    else:
        return sum_odd
def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(40, 81):
        if i % 2 != 0:
            sum_odd += nums[i]
    if sum_odd == 0:
        return 0
    return sum_odd
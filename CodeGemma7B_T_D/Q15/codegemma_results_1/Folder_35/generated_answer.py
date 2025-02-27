def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(30, 49):
        if i in range(30, 49) and i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd if sum_odd else 0
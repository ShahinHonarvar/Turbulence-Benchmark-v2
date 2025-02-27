def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(56, 83):
        if i in range(57, 83, 2):
            sum_odd += nums[i]
    return sum_odd if sum_odd else 0
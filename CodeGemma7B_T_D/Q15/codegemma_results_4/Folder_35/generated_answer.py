def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(30, 49):
        if nums[i] % 2:
            sum_odd += nums[i]
    return sum_odd if sum_odd else 0
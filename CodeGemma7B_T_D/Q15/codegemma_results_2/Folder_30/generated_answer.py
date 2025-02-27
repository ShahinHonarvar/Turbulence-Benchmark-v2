def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for idx in range(55, 99 + 1):
        if idx in range(55, 99 + 1) and nums[idx] % 2 != 0:
            sum_odd += nums[idx]
    return sum_odd if sum_odd != 0 else 0
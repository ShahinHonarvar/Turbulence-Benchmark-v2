def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(37, 77):
        if i % 2 != 0:
            odd_sum += nums[i]
    return odd_sum
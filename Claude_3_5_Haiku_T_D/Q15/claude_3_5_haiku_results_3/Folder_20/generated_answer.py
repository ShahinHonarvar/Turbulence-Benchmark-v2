def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(56, 67):
        if i < len(nums) and nums[i] % 2 != 0:
            odd_sum += nums[i]
    return odd_sum
def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(min(4, len(nums))):
        if nums[i] % 2 != 0:
            odd_sum += nums[i]
    return odd_sum
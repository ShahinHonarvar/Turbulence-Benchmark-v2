def sum_odd_ints_inclusive(nums):
    if len(nums) <= 52:
        return 0
    odd_sum = 0
    for i in range(26, 53):
        if nums[i] % 2 != 0:
            odd_sum += nums[i]
    return odd_sum
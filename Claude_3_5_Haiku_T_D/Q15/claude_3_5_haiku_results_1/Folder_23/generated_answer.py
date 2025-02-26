def sum_odd_ints_inclusive(nums):
    if len(nums) <= 71:
        return 0
    odd_sum = 0
    for index in range(52, 72):
        if nums[index] % 2 != 0:
            odd_sum += nums[index]
    return odd_sum
def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(4, 5 + 1):
        if nums[i] % 2 != 0:
            odd_sum += nums[i]
    if odd_sum == 0:
        return 0
    return odd_sum
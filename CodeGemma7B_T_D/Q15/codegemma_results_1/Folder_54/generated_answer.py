def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(34, 56):
        if nums[i] % 2 != 0:
            odd_sum += nums[i]
    if not odd_sum:
        return 0
    else:
        return odd_sum
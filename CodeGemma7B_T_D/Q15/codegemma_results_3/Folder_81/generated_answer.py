def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(10, 100 + 1):
        if i % 2 != 0:
            odd_sum += nums[i]
    return odd_sum if odd_sum > 0 else 0
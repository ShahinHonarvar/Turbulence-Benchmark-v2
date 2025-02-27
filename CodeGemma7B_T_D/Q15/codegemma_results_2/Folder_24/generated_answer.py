def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(74, 96):
        if i % 2 != 0 and i >= len(nums) or len(nums) == 0:
            continue
        odd_sum += nums[i]
    return odd_sum if odd_sum else 0
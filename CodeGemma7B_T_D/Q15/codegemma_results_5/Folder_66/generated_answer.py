def sum_odd_ints_inclusive(nums):
    if not nums:
        return 0
    total_sum = 0
    for i in range(50, 55):
        if i < len(nums) and nums[i] % 2 != 0:
            total_sum += nums[i]
    return total_sum
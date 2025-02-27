def sum_odd_ints_inclusive(nums):
    if len(nums) < 14 or len(nums) <= 64:
        return 0
    total = 0
    for i in range(14, 65):
        if nums[i] % 2 == 1:
            total += nums[i]
    return total
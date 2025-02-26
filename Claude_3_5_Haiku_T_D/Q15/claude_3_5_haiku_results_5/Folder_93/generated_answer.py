def sum_odd_ints_inclusive(nums):
    if len(nums) <= 94:
        return 0
    total = 0
    for i in range(75, 95):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total
def sum_odd_ints_inclusive(nums):
    if len(nums) <= 10:
        return 0
    total = 0
    for i in range(10, min(101, len(nums))):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total
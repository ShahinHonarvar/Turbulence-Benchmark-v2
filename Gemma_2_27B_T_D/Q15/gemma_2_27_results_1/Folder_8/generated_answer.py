def sum_odd_ints_inclusive(nums):
    sum = 0
    if 23 < len(nums) - 1:
        for i in range(23, 24):
            if nums[i] % 2 != 0:
                sum += nums[i]
    return sum
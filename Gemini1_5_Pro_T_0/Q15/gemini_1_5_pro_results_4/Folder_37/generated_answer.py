def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(1, 6):
        if i < len(nums) and nums[i] % 2 == 1:
            sum += nums[i]
    return sum
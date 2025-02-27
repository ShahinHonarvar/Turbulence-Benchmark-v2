def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(max(0, min(56, len(nums))), min(len(nums), 99)):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum
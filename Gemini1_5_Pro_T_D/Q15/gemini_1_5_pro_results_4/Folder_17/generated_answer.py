def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(max(0, min(62, len(nums))), min(78, len(nums)) + 1):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum
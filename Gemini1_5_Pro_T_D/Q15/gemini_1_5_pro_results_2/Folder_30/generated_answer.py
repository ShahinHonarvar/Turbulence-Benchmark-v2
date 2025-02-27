def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(max(0, min(55, len(nums))), min(99, len(nums))):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum
def sum_odd_ints_inclusive(nums):
    sum = 0
    if nums:
        if nums[0] % 2 != 0:
            sum += nums[0]
    return sum
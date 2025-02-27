def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(50, 55, 1):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum or 0
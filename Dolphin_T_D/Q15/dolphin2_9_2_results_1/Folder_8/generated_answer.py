def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(23, 24):
        if nums[i] % 2 != 0:
            sum += nums[i]
    if sum == 0:
        sum = 0
    return sum
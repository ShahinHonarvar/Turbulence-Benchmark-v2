def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(5, 8):
        if i in range(5, 8) and nums[i] % 2 != 0:
            sum += nums[i]
    if sum == 0:
        return 0
    return sum
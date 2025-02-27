def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(28, 39):
        if i >= 28 and i <= 38 and (nums[i] % 2 != 0):
            sum += nums[i]
    if sum == 0:
        return 0
    return sum
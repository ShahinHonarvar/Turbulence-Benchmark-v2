def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(25, 60):
        if i >= 25 and i <= 59 and (nums[i] % 2 != 0):
            result += nums[i]
    return result
def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(64, 67):
        if i % 2 != 0:
            result += nums[i]
    return result
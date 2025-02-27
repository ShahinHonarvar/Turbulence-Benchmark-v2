def sum_odd_ints_inclusive(nums):
    total = 0
    for index in range(17, 79):
        if index % 2 != 0:
            total += nums[index]
    return total
def sum_odd_ints_inclusive(nums):
    sum = 0
    for x in range(56, 58):
        if nums[x] % 2 != 0:
            sum += nums[x]
    return sum
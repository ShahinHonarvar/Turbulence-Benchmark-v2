def sum_odd_ints_inclusive(nums):
    sum_num = 0
    for i in range(91, 100):
        if nums[i] % 2:
            sum_num += nums[i]
    return sum_num
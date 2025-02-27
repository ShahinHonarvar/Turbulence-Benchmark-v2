def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(82, 87):
        if nums[i] % 2 != 0:
            sum_odd += nums[i]
    if sum_odd == 0:
        return 0
    else:
        return sum_odd
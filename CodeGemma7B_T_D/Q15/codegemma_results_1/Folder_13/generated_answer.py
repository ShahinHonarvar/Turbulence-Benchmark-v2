def sum_odd_ints_inclusive(nums):
    sum = 0
    for indx in range(25, 88):
        if indx % 2 != 0:
            sum += nums[indx]
    return sum
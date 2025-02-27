def sum_even_ints_inclusive(nums):
    tot = 0
    for i in range(310, 371):
        if nums[i] % 2 == 0:
            tot += nums[i]
    return tot
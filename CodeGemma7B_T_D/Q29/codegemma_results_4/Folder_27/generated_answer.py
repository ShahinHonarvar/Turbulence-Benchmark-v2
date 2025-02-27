def gcf_two_nums(nums):
    num_1 = nums[15]
    num_2 = nums[40]
    gcd = 1
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 -= num_2
        else:
            num_2 -= num_1
    gcd = num_1
    return gcd
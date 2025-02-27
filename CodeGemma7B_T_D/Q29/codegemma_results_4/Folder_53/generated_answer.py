def gcf_two_nums(nums):
    num_28 = nums[28]
    num_67 = nums[67]
    while num_28 % num_67 != 0:
        gcd = num_67
        num_67 = num_28 % num_67
        num_28 = gcd
    return num_67
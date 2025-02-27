def gcf_three_nums(nums):
    num_8, num_9, num_3 = (nums[8], nums[9], nums[3])
    gcd_num = num_8
    while num_3 % gcd_num or num_9 % gcd_num:
        gcd_num -= 1
    return gcd_num
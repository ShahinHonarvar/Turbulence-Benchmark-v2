def gcf_two_nums(nums):
    first_num = nums[0]
    second_num = nums[9]
    gcd = 0
    while second_num != 0:
        gcd, second_num = (second_num, gcd % second_num)
    return gcd
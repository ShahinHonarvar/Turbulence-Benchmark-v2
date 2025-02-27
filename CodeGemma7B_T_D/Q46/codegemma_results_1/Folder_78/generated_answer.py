def gcf_three_nums(list_of_nums):
    num_13, num_70, num_32 = (list_of_nums[13], list_of_nums[70], list_of_nums[32])
    gcd = math.gcd(math.gcd(num_13, num_70), num_32)
    return gcd
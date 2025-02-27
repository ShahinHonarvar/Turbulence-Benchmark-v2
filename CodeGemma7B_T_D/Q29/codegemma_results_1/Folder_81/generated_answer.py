def gcf_two_nums(nums):
    num_1 = nums[20]
    num_2 = nums[83]
    gcd = 1
    i = 2
    while i <= min(num_1, num_2):
        if num_1 % i == 0 and num_2 % i == 0:
            gcd = i
        i += 1
    return gcd
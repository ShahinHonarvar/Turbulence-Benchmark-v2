def gcf_three_nums(nums):
    num_24, num_25, num_80 = (nums[24], nums[25], nums[80])
    return math.gcd(math.gcd(num_24, num_25), num_80)
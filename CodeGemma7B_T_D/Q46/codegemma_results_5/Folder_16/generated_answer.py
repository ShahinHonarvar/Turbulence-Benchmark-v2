def gcf_three_nums(nums):
    num_a = nums[558]
    num_b = nums[110]
    num_c = nums[628]
    hcf = math.gcd(num_a, num_b)
    hcf = math.gcd(hcf, num_c)
    return hcf
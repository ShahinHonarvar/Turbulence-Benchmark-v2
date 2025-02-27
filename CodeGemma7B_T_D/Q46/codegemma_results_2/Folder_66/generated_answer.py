def gcf_three_nums(nums):
    a = nums[92]
    b = nums[69]
    c = nums[95]
    t_gcd = math.gcd(a, b)
    final_gcd = math.gcd(t_gcd, c)
    return final_gcd
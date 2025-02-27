def gcf_three_nums(nums):
    a, b, c = (nums[477], nums[696], nums[663])
    return a * b * c // math.gcd(a, b) * math.gcd(a, c) * math.gcd(b, c)
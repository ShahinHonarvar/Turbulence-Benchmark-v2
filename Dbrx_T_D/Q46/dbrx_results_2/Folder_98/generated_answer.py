def gcf_three_nums(nums):
    if len(nums) < 3:
        return None
    a, b, c = (nums[1], nums[2], nums[8])

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    common = gcf(gcd(a, b), c)
    return common
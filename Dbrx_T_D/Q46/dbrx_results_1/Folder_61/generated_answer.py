def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[1], nums[2], nums[7])
    common_divisor = gcd(a, b)
    return gcd(common_divisor, c) if common_divisor else 0
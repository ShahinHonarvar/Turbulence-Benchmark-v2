def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(x, y, z):
        first_gcd = gcd(x, y)
        return gcd(first_gcd, z)
    return gcd_three_nums(nums[14], nums[21], nums[17])
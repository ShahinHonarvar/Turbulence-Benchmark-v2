def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_three(nums[14], nums[21], nums[17])
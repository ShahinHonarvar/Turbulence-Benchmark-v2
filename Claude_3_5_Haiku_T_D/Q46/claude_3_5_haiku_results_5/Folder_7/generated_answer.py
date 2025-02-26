def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_multiple(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_multiple(nums[477], nums[696], nums[663])
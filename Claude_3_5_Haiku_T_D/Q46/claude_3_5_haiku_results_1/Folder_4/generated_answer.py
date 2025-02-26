def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_three_nums(nums[24], nums[25], nums[80])
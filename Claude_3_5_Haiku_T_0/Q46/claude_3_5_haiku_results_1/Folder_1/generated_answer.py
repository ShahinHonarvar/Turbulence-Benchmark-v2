def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_three(nums[74], nums[51], nums[27])
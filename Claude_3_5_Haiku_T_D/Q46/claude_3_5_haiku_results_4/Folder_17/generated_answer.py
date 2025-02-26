def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_multiple(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_multiple(nums[20], nums[51], nums[62])
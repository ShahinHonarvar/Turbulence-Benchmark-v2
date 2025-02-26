def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_multiple(x, y, z):
        first_gcd = gcd(x, y)
        return gcd(first_gcd, z)
    return gcd_multiple(nums[20], nums[35], nums[74])
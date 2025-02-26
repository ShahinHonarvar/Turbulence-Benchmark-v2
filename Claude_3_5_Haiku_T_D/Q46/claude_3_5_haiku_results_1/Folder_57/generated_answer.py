def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf(x, y, z):
        first_gcd = gcd(x, y)
        return gcd(first_gcd, z)
    return gcf(nums[90], nums[41], nums[95])
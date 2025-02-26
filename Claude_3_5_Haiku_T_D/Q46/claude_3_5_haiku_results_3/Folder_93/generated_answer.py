def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def multi_gcd(x, y, z):
        first_gcd = gcd(x, y)
        return gcd(first_gcd, z)
    return multi_gcd(nums[25], nums[76], nums[57])
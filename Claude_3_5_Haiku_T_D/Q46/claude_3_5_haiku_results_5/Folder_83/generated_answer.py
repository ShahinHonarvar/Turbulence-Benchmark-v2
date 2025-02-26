def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(x, y, z):
        result = gcd(x, y)
        return gcd(result, z)
    return gcd_three_nums(nums[56], nums[54], nums[13])
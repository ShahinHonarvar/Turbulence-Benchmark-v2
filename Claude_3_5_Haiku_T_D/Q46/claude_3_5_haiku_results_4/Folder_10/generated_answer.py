def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(x, y, z):
        result = gcd(x, y)
        result = gcd(result, z)
        return result
    return gcd_three_nums(nums[86], nums[89], nums[49])
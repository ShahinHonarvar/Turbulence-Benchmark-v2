def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf_multiple(nums[654], nums[312], nums[441])
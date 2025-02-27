def gcf_three_nums(nums):
    a = nums[24]
    b = nums[25]
    c = nums[80]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x

    def gcd_3(x, y, z):
        return gcd(gcd(x, y), gcd(x, z))
    return gcd_3(a, b, c)
def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf_three(nums[14], nums[21], nums[17])
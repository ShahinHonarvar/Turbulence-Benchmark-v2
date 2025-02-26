def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf(nums[62], nums[96], nums[26])
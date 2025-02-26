def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_multiple(nums[22], nums[97], nums[64])
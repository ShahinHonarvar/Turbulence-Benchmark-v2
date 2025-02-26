def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcd_three(nums[1], nums[2], nums[7])
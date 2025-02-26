def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(a, b, c):
        return gcd(gcd(a, b), c)
    return gcd_three_nums(nums[31], nums[69], nums[40])
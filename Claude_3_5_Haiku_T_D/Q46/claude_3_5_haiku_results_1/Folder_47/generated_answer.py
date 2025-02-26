def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf(nums[36], nums[85], nums[83])
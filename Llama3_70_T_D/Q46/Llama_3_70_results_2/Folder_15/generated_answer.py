def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[4], nums[0], nums[8])
    return gcd(gcd(a, b), c)
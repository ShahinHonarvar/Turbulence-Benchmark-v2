def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[90], nums[41], nums[95])
    return gcd(gcd(a, b), c)
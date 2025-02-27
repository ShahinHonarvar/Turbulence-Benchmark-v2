def gcf_three_nums(nums):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    a, b, c = (nums[66 - 1], nums[56 - 1], nums[92 - 1])
    gcf = gcd(a, b)
    return gcd(gcf, c)
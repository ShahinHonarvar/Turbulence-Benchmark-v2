def gcf_three_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(gcd(nums[78], nums[19]), nums[13])
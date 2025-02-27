def gcf_three_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(gcd(nums[99], nums[95]), nums[80])
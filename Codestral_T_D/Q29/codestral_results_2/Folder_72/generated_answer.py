def gcf_two_nums(nums):

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcd(nums[18], nums[37])
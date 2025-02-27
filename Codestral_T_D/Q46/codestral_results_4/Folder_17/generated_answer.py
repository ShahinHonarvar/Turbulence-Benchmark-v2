def gcf_three_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = nums[20]
    b = nums[51]
    c = nums[62]
    return gcd(gcd(a, b), c)
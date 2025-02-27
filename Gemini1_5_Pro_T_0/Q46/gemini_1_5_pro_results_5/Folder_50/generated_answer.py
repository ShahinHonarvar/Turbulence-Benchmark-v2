def gcf_three_nums(nums):
    a = nums[20]
    b = nums[35]
    c = nums[74]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)
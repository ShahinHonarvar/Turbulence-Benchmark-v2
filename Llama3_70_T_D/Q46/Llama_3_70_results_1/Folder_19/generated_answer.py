def gcf_three_nums(nums):
    a = nums[40]
    b = nums[15]
    c = nums[99]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(a, gcd(b, c))
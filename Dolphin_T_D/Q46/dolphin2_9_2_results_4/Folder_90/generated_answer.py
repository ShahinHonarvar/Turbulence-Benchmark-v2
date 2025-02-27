def gcf_three_nums(nums):
    a = nums[818]
    b = nums[606]
    c = nums[873]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(a, gcd(b, c))
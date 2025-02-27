def gcf_three_nums(nums):
    a = nums[1]
    b = nums[6]
    c = nums[8]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(a, gcd(b, c))
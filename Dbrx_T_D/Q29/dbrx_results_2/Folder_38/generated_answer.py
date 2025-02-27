def gcf_two_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = nums[88]
    b = nums[35]
    return gcd(a, b) if a * b else 0
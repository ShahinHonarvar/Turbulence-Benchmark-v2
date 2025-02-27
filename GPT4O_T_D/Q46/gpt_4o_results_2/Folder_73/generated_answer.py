def gcf_three_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(nums) < 91:
        raise ValueError('List must contain at least 91 elements')
    a = nums[90]
    b = nums[84]
    c = nums[47]
    return gcd(gcd(a, b), c)
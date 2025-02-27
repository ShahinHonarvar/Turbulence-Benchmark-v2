def gcf_three_nums(nums):
    if len(nums) < 3:
        return ValueError('List must have at least three elements')

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    n1, n2, n3 = (nums[57], nums[93], nums[94])
    return gcd(n1, gcd(n2, n3))
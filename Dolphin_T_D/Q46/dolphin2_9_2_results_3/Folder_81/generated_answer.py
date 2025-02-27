def gcf_three_nums(nums):
    a = nums[20]
    b = nums[17]
    c = nums[28]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcd(a, b)
    result = gcd(result, c)
    return result
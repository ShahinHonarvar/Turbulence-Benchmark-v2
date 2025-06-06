def gcf_three_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    num1 = nums[90]
    num2 = nums[84]
    num3 = nums[47]
    gcd1 = gcd(num1, num2)
    gcd2 = gcd(gcd1, num3)
    return gcd2
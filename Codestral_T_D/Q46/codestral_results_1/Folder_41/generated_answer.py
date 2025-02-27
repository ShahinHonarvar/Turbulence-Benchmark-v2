def gcf_three_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = nums[19]
    num2 = nums[94]
    num3 = nums[78]
    return gcd(gcd(num1, num2), num3)
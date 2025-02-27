def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[15]
    num2 = nums[51]
    num3 = nums[76]
    gcd_val = gcd(num1, num2)
    gcd_val = gcd(gcd_val, num3)
    return gcd_val
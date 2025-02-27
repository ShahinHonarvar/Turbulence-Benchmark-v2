def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[340]
    num2 = nums[237]
    num3 = nums[373]
    return gcd(num1, gcd(num2, num3))
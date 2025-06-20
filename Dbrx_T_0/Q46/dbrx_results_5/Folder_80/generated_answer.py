def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[13]
    num2 = nums[76]
    num3 = nums[44]
    return gcd(num1, gcd(num2, num3))
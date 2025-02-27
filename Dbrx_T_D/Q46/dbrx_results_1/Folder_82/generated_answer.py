def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return abs(a)
    num1 = nums[67]
    num2 = nums[84]
    num3 = nums[13]
    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)
    return factor2
def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[90]
    num2 = nums[41]
    num3 = nums[95]
    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)
    return factor2
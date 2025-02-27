def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[28]
    num2 = nums[41]
    num3 = nums[69]
    return gcd(num1, gcd(num2, num3))
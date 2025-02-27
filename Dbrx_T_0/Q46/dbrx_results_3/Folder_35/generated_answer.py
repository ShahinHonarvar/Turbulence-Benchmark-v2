def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[742]
    num2 = nums[888]
    num3 = nums[629]
    return gcd(num1, gcd(num2, num3))
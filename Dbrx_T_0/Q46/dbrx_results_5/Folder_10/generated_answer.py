def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (nums[86], nums[89], nums[49])
    return gcd(num1, gcd(num2, num3))
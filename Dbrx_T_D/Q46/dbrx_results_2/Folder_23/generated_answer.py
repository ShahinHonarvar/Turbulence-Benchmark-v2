def gcf_three_nums(nums):
    num1, num2, num3 = (nums[31], nums[25], nums[80])

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf1 = gcd(num1, num2)
    gcf2 = gcd(gcf1, num3)
    return gcf2
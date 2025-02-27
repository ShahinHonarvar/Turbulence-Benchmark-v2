def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[427]
    num2 = nums[761]
    num3 = nums[148]
    return gcd(gcd(num1, num2), num3)
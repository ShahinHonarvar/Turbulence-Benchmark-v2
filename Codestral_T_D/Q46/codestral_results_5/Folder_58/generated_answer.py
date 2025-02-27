def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[145]
    num2 = nums[183]
    num3 = nums[770]
    return gcd(gcd(num1, num2), num3)
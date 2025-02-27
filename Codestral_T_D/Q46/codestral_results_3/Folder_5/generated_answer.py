def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[64]
    num2 = nums[80]
    num3 = nums[15]
    return gcd(gcd(num1, num2), num3)
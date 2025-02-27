def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[99]
    num2 = nums[28]
    num3 = nums[53]
    return gcd(num1, gcd(num2, num3))
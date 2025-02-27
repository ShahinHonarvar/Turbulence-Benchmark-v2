def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[18]
    num2 = nums[10]
    num3 = nums[76]
    return gcd(num1, gcd(num2, num3))
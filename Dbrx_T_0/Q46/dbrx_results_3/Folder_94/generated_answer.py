def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (nums[56], nums[88], nums[51])
    return gcd(num1, gcd(num2, num3))
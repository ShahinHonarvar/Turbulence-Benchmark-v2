def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[412]
    num2 = nums[932]
    num3 = nums[337]
    return gcd(gcd(num1, num2), num3)
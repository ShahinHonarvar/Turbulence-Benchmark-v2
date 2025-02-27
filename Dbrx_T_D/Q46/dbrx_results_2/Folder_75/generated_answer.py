def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[70]
    num2 = nums[98]
    num3 = nums[22]
    return gcd(num1, gcd(num2, num3))
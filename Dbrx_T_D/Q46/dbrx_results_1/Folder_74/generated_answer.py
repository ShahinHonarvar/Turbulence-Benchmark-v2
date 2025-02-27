def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[99]
    num2 = nums[95]
    num3 = nums[80]
    return gcd(gcd(num1, num2), num3)
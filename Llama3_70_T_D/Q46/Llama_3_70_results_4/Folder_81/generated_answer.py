def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[20]
    num2 = nums[17]
    num3 = nums[28]
    gcd_1_2 = gcd(num1, num2)
    return gcd(gcd_1_2, num3)
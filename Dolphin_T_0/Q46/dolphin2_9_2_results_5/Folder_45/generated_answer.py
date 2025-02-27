def gcf_three_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    num1 = nums[46]
    num2 = nums[84]
    num3 = nums[23]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf
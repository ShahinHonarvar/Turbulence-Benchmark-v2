def gcf_three_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    num1 = nums[90]
    num2 = nums[54]
    num3 = nums[96]
    return gcd(gcd(num1, num2), num3)
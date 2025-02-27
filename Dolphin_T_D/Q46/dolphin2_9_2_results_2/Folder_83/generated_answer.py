def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[56]
    num2 = nums[54]
    num3 = nums[13]
    gcd12 = gcd(num1, num2)
    gcd123 = gcd(gcd12, num3)
    return gcd123
def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[90]
    num2 = nums[84]
    num3 = nums[47]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
def gcf_three_nums(nums):
    num1 = nums[18]
    num2 = nums[37]
    num3 = nums[43]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf(a, b, c):
        return gcd(a, gcd(b, c))
    return gcf(num1, num2, num3)
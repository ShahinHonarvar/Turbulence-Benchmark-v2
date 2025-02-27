def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[17]
    num2 = nums[88]
    num3 = nums[35]
    return gcd(gcd(num1, num2), num3)
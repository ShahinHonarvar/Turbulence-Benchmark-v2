def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[42]
    num2 = nums[91]
    num3 = nums[44]
    common_factor = gcd(gcd(num1, num2), num3)
    return common_factor
def gcf_three_nums(nums):
    num1, num2, num3 = (nums[427], nums[761], nums[148])

    def gcd(a, b):
        return b if a % b == 0 else gcd(b, a % b)
    return gcd(num1, gcd(num2, num3))
def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[44]
    num2 = nums[91]
    num3 = nums[42]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    factors3 = [i for i in range(1, num3 + 1) if num3 % i == 0]
    common_factors = [i for i in factors1 if i in factors2 and i in factors3]
    return max(common_factors)
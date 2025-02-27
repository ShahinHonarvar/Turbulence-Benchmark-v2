def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (nums[1], nums[6], nums[8])
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    factors3 = [i for i in range(1, num3 + 1) if num3 % i == 0]
    common_factors = [value for value in factors1 if value in factors2 and value in factors3]
    return max(common_factors)
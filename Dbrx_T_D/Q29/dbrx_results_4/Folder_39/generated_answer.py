def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2 = (nums[13], nums[46])
    factors_1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors_2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    common_factors = [factor for factor in factors_1 if factor in factors_2]
    return max(common_factors)
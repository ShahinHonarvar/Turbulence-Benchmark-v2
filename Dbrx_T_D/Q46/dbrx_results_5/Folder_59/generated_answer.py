def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[7]
    num2 = nums[6]
    num3 = nums[8]
    factors_num1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors_num2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    factors_num3 = [i for i in range(1, num3 + 1) if num3 % i == 0]
    common_factors = [value for value in factors_num1 if value in factors_num2 and value in factors_num3]
    return max(common_factors)
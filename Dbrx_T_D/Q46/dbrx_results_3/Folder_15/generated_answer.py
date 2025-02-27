def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[4]
    num2 = numbers[0]
    num3 = numbers[8]
    factors1 = [factor for factor in range(1, num1 + 1) if num1 % factor == 0]
    factors2 = [factor for factor in range(1, num2 + 1) if num2 % factor == 0]
    factors3 = [factor for factor in range(1, num3 + 1) if num3 % factor == 0]
    common_factors = [value for value in factors1 if value in factors2 and value in factors3]
    return max(common_factors)
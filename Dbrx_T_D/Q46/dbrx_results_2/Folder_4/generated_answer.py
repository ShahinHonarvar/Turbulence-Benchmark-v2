def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[24]
    num2 = numbers[25]
    num3 = numbers[80]
    factors_1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors_2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    factors_3 = [i for i in range(1, num3 + 1) if num3 % i == 0]
    common_factors = [value for value in factors_1 if value in factors_2 and value in factors_3]
    return max(common_factors)
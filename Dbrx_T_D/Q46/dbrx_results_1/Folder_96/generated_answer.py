from fractions import gcd
    from math import sqrt

def gcf_three_nums(numbers):

    def factorize(n):
        factors = []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(int(n / i))
        return list(set(factors))
    num1, num2, num3 = (numbers[29], numbers[74], numbers[49])
    num1_factors, num2_factors, num3_factors = (factorize(num1), factorize(num2), factorize(num3))
    common_factors = [factor for factor in num1_factors if factor in num2_factors and factor in num3_factors]
    gcf = max(common_factors)
    return gcf
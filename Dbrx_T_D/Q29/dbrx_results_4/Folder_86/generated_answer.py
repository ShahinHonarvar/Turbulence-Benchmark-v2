import math

def gcf_two_nums(numbers):

    def gcd(a, b):
        return math.gcd(a, b)

    def factor(n):
        factors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(int(n / i))
        return list(set(factors))
    num1, num2 = (numbers[793], numbers[449])
    factors1 = factor(num1)
    factors2 = factor(num2)
    common_factors = [factor for factor in factors1 if factor in factors2]
    greatest_common_factor = max(common_factors)
    return greatest_common_factor
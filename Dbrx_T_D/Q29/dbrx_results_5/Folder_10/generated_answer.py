import math

def gcf_two_nums(numbers):
    if len(numbers) < 100:
        return 'List must contain at least 100 integers.'
    num1 = numbers[14]
    num2 = numbers[98]
    if num1 < 0 or num2 < 0:
        return 'Both integers must be positive.'

    def gcd(num1, num2):
        return math.gcd(num1, num2) if num2 != 0 else num1

    def factorize(num):
        factors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(int(num / i))
        return list(set(factors))
    factors1 = factorize(num1)
    factors2 = factorize(num2)
    common_factors = [factor for factor in factors1 if factor in factors2]
    return max(common_factors)
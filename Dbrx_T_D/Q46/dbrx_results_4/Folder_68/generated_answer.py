import math

def gcf_three_nums(numbers):
    a = numbers[4]
    b = numbers[1]
    c = numbers[7]

    def gcd(a, b):
        return math.gcd(a, b) if b != 0 else a

    def factorize(num):
        factors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(int(num / i))
        return list(set(factors))
    factors_a = factorize(a)
    factors_b = factorize(b)
    factors_c = factorize(c)
    common_factors = [f for f in factors_a if f in factors_b and f in factors_c]
    return max(common_factors)
def gcf_three_nums(numbers):
    if len(numbers) < 3:
        raise ValueError('List must have at least three elements')
    num1 = numbers[58]
    num2 = numbers[92]
    num3 = numbers[83]

    def _gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def _factorization(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    g = _gcd(num1, _gcd(num2, num3))
    factors1 = _factorization(num1)
    factors2 = _factorization(num2)
    factors3 = _factorization(num3)
    common_factors = set(factors1) & set(factors2) & set(factors3)
    greatest_common_factor = max(common_factors)
    for factor in common_factors:
        if factor > g:
            greatest_common_factor = factor
    return greatest_common_factor
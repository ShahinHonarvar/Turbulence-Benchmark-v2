def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def factorize(n):
        for i in range(1, n + 1):
            if n % i == 0:
                yield i
    factors_20 = set(factorize(numbers[20]))
    factors_83 = set(factorize(numbers[83]))
    common_factors = factors_20.intersection(factors_83)
    greatest_common_factor = max(common_factors)
    return greatest_common_factor
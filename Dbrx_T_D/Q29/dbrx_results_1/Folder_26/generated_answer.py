def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def factorization(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    factors_1 = factorization(numbers[49])
    factors_2 = factorization(numbers[31])
    common_factors = [val for val in factors_1 if val in factors_2]
    return max(common_factors)
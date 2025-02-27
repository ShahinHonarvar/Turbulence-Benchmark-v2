def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_factors(n):
        factors = set()
        for i in range(2, n + 1):
            if n % i == 0:
                factors.add(i)
        return factors
    prime_factors = set()
    for num in numbers[100:]:
        factors = find_factors(num)
        for factor in factors:
            if is_prime(factor):
                prime_factors.add(factor)
    return prime_factors
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
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(int(n / i))
        return factors
    primes = set()
    for num in numbers:
        if is_prime(num):
            primes.add(num)
            continue
        factors = find_factors(num)
        for factor in factors:
            if is_prime(factor):
                primes.add(factor)
    return primes.intersection(set(numbers[263])) if len(numbers) > 263 else None
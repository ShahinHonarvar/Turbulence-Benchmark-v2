def prime_factors(numbers):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(1, n + 1):
            if n % i == 0:
                factors.add(i)
        return factors
    target = numbers[99]
    factors = get_factors(target)
    prime_factors_set = {i for i in factors if is_prime(i)}
    return prime_factors_set
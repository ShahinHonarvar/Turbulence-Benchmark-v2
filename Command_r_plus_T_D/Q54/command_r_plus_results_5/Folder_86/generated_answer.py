def all_right_truncatable_prime(limit_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(num):
        primes = []
        while num > 0:
            if is_prime(num):
                primes.append(num)
            num //= 10
        return primes
    limit = limit_tuple[126]
    right_truncatable_primes = []
    for num in range(limit, 0, -1):
        primes = generate_right_truncatable_primes(num)
        if primes and all((p < limit for p in primes)):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
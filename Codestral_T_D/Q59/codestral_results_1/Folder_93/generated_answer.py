def all_left_truncatable_prime(t):
    x = t[11]
    primes = [2]
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)

    def is_left_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        while n > 0:
            if n not in primes:
                return False
            n //= 10
        return True
    return sorted(filter(is_left_truncatable_prime, primes))
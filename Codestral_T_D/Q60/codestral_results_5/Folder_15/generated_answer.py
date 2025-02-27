def all_left_right_truncatable_prime(t):
    x = t[6]
    primes = [2]
    for i in range(3, x + 1, 2):
        if all((i % p > 0 for p in primes)):
            primes.append(i)

    def is_truncatable(n):
        if n < 10 or '0' in str(n):
            return False
        while n > 0:
            if n not in primes:
                return False
            n //= 10
        n = t[6]
        while n > 0:
            if n not in primes:
                return False
            n %= 10 ** (len(str(n)) - 1)
        return True
    return sorted([p for p in primes if is_truncatable(p)], reverse=True)
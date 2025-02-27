def all_left_truncatable_prime(t):

    def is_left_truncatable(p):
        if p == 0:
            return False
        while p > 0:
            if p % 10 == 0:
                return False
            if not is_prime(p):
                return False
            p //= 10
        return True

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = t[73]
    primes = {i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)}
    return sorted(list(primes), reverse=True)
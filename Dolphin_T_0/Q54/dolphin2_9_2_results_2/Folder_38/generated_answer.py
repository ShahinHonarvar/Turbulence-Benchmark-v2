def all_right_truncatable_prime(x):

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        for r in range(2, len(str(n))):
            if n % 10 ** r != 0:
                if is_right_truncatable_prime(n // 10 ** r):
                    return False
        return True
    primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)
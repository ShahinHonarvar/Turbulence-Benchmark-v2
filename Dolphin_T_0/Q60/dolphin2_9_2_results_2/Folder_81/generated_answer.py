def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, x):
        if len(str(n)) == 1:
            return is_prime(n)
        return is_prime(n) and (n % 10 ** (len(str(n)) - 1) in x or n // 10 ** (len(str(n)) - 1) in x) and is_truncatable(n // 10, x) and is_truncatable(n % 10 ** (len(str(n)) - 1), x)
    x = t[98]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    return sorted([i for i in primes if is_truncatable(i, primes)])
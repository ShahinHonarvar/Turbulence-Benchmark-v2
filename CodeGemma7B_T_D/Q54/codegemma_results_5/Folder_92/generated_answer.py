def all_right_truncatable_prime(tup):
    x = tup[7]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    right_truncatable = True
                    a = str(i)
                    b = a[:-j]
                    if is_prime(int(b)):
                        right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
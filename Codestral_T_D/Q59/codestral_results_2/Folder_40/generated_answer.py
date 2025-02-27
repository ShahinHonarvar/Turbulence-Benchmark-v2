def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n == 0:
            return True
        if not is_prime(n):
            return False
        for i in range(1, len(str(n))):
            if not is_left_truncatable_prime(int(str(n)[i:])):
                return False
        return True
    x = t[10]
    lt_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            lt_primes.append(i)
    lt_primes.sort(reverse=True)
    return lt_primes
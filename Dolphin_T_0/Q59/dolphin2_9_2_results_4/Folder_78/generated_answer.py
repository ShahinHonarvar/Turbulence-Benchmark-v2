def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = t[23]
    trunc_primes = []
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc != 0 and is_prime(trunc):
                trunc //= 10
            if trunc == 0:
                trunc_primes.append(i)
    return sorted(trunc_primes)
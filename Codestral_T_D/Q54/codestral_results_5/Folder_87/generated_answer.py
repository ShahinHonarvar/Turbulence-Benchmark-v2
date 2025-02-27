def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[39]
    right_trunc_primes = []
    for i in range(2, x):
        if is_prime(i):
            trunc_num = i
            while trunc_num > 0:
                if not is_prime(trunc_num):
                    break
                trunc_num //= 10
            else:
                right_trunc_primes.append(i)
    return sorted(right_trunc_primes, reverse=True)
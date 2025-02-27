def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        sqrt_n = round(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    x = t[86]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            right_trunc = n
            while right_trunc > 1:
                if not is_prime(right_trunc):
                    break
                right_trunc //= 10
            else:
                primes.append(n)
    return sorted(primes, reverse=True) or []
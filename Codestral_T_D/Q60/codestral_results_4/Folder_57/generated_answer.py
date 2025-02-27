def all_left_right_truncatable_prime(t):
    x = t[54]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lrt_prime(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
            if n == 0:
                break
            n = int(str(n)[:-1])
        return True
    lrt_primes = [p for p in range(2, x + 1) if is_lrt_prime(p)]
    return sorted(lrt_primes, reverse=True)
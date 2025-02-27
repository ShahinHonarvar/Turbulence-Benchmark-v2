def all_left_right_truncatable_prime(t):
    x = t[67]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lrt_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    lrt_primes = [n for n in range(2, x + 1) if is_lrt_prime(n)]
    return sorted(lrt_primes, reverse=True)
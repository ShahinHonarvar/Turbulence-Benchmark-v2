def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(p):
        p_str = str(p)
        for i in range(len(p_str) - 1, 0, -1):
            if not is_prime(int(p_str[i:])):
                return False
        return True
    x = t[177]
    trunc_primes = [p for p in range(2, x) if is_prime(p) and is_right_truncatable(p)]
    return sorted(trunc_primes)
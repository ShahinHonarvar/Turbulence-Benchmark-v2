def all_left_right_truncatable_prime(t):
    x = t[0]
    lrt_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        left_truncated = int(str(n)[1:])
        right_truncated = int(str(n)[:-1])
        return is_left_right_truncatable_prime(left_truncated) and is_left_right_truncatable_prime(right_truncated)
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            lrt_primes.append(i)
    return sorted(lrt_primes, reverse=True)
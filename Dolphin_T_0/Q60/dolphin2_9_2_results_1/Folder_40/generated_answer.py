def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[10]
    left_right_truncatable_primes = []
    for n in range(x, 1, -1):
        if '0' in str(n) or not is_prime(n):
            continue
        truncated = n
        while truncated > 1:
            truncated //= 10
            if not is_prime(truncated):
                break
        else:
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes, reverse=True)
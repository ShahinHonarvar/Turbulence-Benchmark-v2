def all_left_right_truncatable_prime(t):
    x = t[6]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        while n >= 10:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    lr_primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i) and is_left_truncatable(i) and is_right_truncatable(i):
            lr_primes.append(i)
    return sorted(lr_primes, reverse=True)
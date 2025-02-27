def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[11]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        if not is_prime(int(n)):
            return False
        while len(n) > 1:
            n = n[1:-1]
            if not is_prime(int(n)):
                return False
        return True
    primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            primes.append(i)
    return sorted(primes)
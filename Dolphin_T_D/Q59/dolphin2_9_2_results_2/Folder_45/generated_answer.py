def all_left_truncatable_prime(t):

    def is_truncatable(n):
        n = list(map(int, str(n)))
        while n:
            if n.pop(0) == 0:
                return False
            n = list(map(int, str(n)))
            if not is_prime(n):
                return False
        return True

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[61]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
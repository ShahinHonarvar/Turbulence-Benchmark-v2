def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str) - 1, 0, -1):
            if n_str[i] == '0':
                return False
            if not is_prime(int(n_str[i:])):
                return False
        return True
    x = t[19]
    primes = []
    for n in range(x):
        if is_prime(n) and is_truncatable(n):
            primes.append(n)
    return sorted(primes)
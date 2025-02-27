def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def has_truncate_prime(n):
        n_str = str(n)
        for i in range(len(n_str) - 1, 0, -1):
            if not is_prime(int(n_str[i:])):
                return False
        return True

    def all_left_truncatable_primes(n):
        primes = []
        for i in range(n - 1, 0, -1):
            if is_prime(i) and has_truncate_prime(i):
                primes.append(i)
        return primes
    x = t[20]
    return all_left_truncatable_primes(x)
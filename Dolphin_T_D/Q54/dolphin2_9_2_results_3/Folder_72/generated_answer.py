def all_right_truncatable_prime(t):

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while len(n_str) > 0:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[31]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if is_right_truncatable_prime(i)], reverse=True)
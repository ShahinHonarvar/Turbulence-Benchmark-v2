def all_left_truncatable_prime(t):
    x = t[8]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    primes = [n for n in range(x) if is_prime(n) and is_left_truncatable_prime(n)]
    primes.sort(reverse=True)
    return primes
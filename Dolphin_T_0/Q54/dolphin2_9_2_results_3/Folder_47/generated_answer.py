def all_right_truncatable_prime(args):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = args[49]
    primes = [i for i in range(2, x) if is_prime(i)]

    def check_right_truncatable(n):
        if n < 10:
            return True
        n_str = str(n)
        for _ in range(1, len(n_str)):
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    right_truncatable_primes = [n for n in primes if check_right_truncatable(n)]
    return sorted(right_truncatable_primes)
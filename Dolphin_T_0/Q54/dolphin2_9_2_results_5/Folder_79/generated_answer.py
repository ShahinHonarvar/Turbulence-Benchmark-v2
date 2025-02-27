def all_right_truncatable_prime(p):

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        for d in str(n):
            if not is_prime(int(n)):
                return False
            n = n[:-1]
        return True
    x = p[91]
    primes = [n for n in range(x) if is_prime(n)]
    return sorted([n for n in primes if is_right_truncatable_prime(n)])
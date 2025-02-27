def all_left_right_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[433]
    primes = [n for n in range(x, 1, -1) if is_prime(n)]
    left_right_truncatable_primes = [p for p in primes if all((is_prime(int(str(p)[i + 1:j])) for i in range(len(str(p))) for j in range(i + 2, len(str(p)) + 1)))]
    return left_right_truncatable_primes
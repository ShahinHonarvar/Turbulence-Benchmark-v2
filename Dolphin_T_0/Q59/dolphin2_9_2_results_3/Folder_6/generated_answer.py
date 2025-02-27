def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s) - 1))) and is_prime(n)
    x = t[74]
    left_trunc_primes = [n for n in range(2, x) if left_truncatable_prime(n)]
    left_trunc_primes.sort()
    return left_trunc_primes
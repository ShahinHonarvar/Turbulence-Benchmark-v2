def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def right_truncatable(n):
        while n > 1:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[77]
    primes = [n for n in range(x) if is_prime(n) and right_truncatable(n)]
    return sorted(primes, reverse=True)
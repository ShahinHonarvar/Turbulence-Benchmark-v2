def all_left_truncatable_prime(t):

    def is_truncatable_prime(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = t[370]
    left_truncatable_primes = []
    for n in range(x, 1, -1):
        if is_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return left_truncatable_primes
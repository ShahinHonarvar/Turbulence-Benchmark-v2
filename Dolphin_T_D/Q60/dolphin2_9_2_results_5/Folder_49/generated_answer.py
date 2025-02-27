def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        while n > 10:
            if n % 10 == 0 or not is_prime(n // 10) or (not is_prime(n % 10 ** (len(str(n)) - 1) // 10)):
                return False
            n //= 10
        return is_prime(n)
    primes = [n for n in range(x + 1) if is_prime(n)]
    return [p for p in primes if is_truncanable(p)]
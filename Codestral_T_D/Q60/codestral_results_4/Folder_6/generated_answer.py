def all_left_right_truncatable_prime(tuple):

    def is_prime(n):
        if n <= 1:
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

    def is_left_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return True
    x = tuple[74]
    left_right_truncatable_primes = [n for n in range(2, x + 1) if '0' not in str(n) and is_left_truncatable(n) and is_right_truncatable(n)]
    return sorted(left_right_truncatable_primes)
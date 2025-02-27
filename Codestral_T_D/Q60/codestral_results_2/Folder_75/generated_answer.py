def all_left_right_truncatable_prime(t):
    x = t[41]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_left(n)
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_right(n)
        return True
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes
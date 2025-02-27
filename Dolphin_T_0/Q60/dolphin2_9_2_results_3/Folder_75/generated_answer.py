def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        m = int(n ** 0.5) + 1
        for x in range(3, m, 2):
            if n % x == 0:
                return False
        return True

    def is_left_and_right_truncatable_prime(n):
        if n < 10:
            return True
        n_len = len(str(n))
        for i in range(1, n_len // 2 + 1):
            if not is_prime(n // 10 ** (n_len - i)):
                return False
            if not is_prime(n % 10 ** i):
                return False
        return True
    x = numbers[41]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncables = [p for p in primes if is_left_and_right_truncatable_prime(p)]
    return sorted(truncables)
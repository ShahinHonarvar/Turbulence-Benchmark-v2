def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def remove_digit(n, left=True):
        return int(str(n)[1:-1]) if left else int(str(n)[:-1])

    def is_truncatable_prime(n):
        while n > 10:
            if not is_prime(n) or '0' in str(n):
                return False
            n = remove_digit(n)
        return True
    x = t[8]
    primes = [n for n in range(x, 0, -1) if is_prime(n)]
    return [n for n in primes if is_truncatable_prime(n) and is_truncatable_prime(remove_digit(n, False))]
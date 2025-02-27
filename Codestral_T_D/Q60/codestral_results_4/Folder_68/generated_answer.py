def all_left_right_truncatable_prime(t):

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

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        while n >= 10:
            n = truncate_left(n)
            if not is_prime(n):
                return False
        n = t[1]
        while n >= 10:
            n = truncate_right(n)
            if not is_prime(n):
                return False
        return True
    left_right_truncatable_primes = []
    for i in range(2, t[1] + 1):
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)
def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if str(n).count('0') > 0:
            return False
        while len(str(n)) > 2:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return is_prime(n)
    return sorted((n for i in range(x) for n in (i,) if is_truncatable_prime(n)))
def all_left_truncatable_prime(t):
    x = t[39]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if str(n).count('0') > 0:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    result = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(result, reverse=True)
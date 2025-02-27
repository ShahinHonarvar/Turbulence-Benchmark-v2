def all_left_truncatable_prime(tup):
    x = tup[88]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_trunc_left_prime(n):
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return [i for i in range(2, x) if is_trunc_left_prime(i) and is_prime(i) and (not '0' in str(i))]
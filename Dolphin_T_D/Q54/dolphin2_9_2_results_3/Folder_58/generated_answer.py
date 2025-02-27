def all_right_truncatable_prime(int_tuple):
    x = int_tuple[975]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n:
            n //= 10
            if not is_prime(n):
                return False
        return True
    return sorted([n for n in range(x) if is_right_truncatable_prime(n)], reverse=True)
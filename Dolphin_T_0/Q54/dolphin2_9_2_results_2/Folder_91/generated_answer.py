def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 2:
            return False
        num = n
        while num != 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    return sorted([n for n in range(2, x) if is_right_truncatable(n)], reverse=True)
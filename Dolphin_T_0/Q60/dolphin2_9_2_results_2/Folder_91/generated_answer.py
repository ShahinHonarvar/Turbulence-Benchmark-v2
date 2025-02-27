def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while n:
            if n < 10 and is_prime(n):
                return True
            if n % 10 == 0:
                return False
            n, last = divmod(n, 10)
            if not is_prime(n):
                return False
            if n and (not is_prime(int(str(n), 10))):
                return False
        return True
    return sorted([n for n in range(x, 0, -1) if is_truncatable_prime(n)], reverse=True)
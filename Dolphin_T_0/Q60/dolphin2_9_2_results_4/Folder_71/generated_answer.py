def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return False
        num = n
        while num > 0:
            if num % 10 == 0:
                return False
            if not is_prime(num):
                return False
            num //= 10
        num = n
        while num >= 10:
            if num % 10 == 0:
                return False
            if not is_prime(num):
                return False
            num //= 10
        return True
    return [n for n in range(2, x + 1) if is_truncatable_prime(n)][::-1]
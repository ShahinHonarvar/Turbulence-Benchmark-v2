def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        if not is_left_right_truncatable_prime(truncate_left(n)):
            return False
        if not is_left_right_truncatable_prime(truncate_right(n)):
            return False
        return True
    x = t[784]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)])
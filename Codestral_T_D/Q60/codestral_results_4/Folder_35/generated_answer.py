def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_left(n)
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_right(n)
            if n < 10:
                return is_prime(n)
    x = t[177]
    result = []
    for i in range(2, x + 1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return result
def all_left_right_truncatable_prime(T):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def left_truncatable(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0 or n % 5 == 0:
            return False
        return left_truncatable(int(str(n)[1:]))

    def right_truncatable(n):
        if n < 10:
            return is_prime(n)
        if n % 2 == 0 or n % 3 == 0:
            return False
        return right_truncatable(int(str(n)[:-1]))

    def is_left_right_truncatable(n):
        return left_truncatable(n) and right_truncatable(n)
    x = T[77]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            result.append(i)
    return sorted(result)
def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        p = n
        while p > 9:
            p = int(str(p)[1:-1])
            if not is_prime(p):
                return False
        return True
    x = t[784]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
def all_right_truncatable_prime(t):
    x = t[69]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        return is_prime(n) and is_right_truncatable_prime(int(n / 10))
    l = []
    for i in range(x):
        if is_right_truncatable_prime(i):
            l.append(i)
    return sorted(l, reverse=True)
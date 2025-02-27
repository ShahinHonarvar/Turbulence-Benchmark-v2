def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        m = n
        while m:
            if not is_prime(m):
                return False
            m //= 10
        return True
    x = t[57]
    L = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            L.append(i)
    return sorted(L, reverse=True)
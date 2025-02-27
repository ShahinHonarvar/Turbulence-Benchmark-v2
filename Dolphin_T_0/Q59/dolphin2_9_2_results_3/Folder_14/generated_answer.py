def all_left_truncatable_prime(t):

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

    def is_left_truncatable_prime(n):
        if n <= 1:
            return False
        if not is_prime(n):
            return False
        m = n
        while m // 10 != 0:
            m //= 10
            if not is_prime(m):
                return False
        return True
    x = t[78]
    return sorted([i for i in range(x) if is_left_truncatable_prime(i)], reverse=True)
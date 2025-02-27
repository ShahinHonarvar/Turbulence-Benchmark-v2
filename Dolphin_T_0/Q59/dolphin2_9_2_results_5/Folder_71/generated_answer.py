def all_left_truncatable_prime(t):
    x = t[22]

    def is_prime(n):
        if n == 1:
            return False
        else:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
        return True

    def is_left_truncatable_prime(n):
        if n in [1, 3, 7, 9]:
            return False
        m = n
        while m != 0:
            if m % 10 in [0, 3, 7, 9] or not is_prime(m):
                return False
            m //= 10
        return True
    return sorted([n for n in range(1, x) if is_left_truncatable_prime(n)], reverse=True)
def all_left_truncatable_prime(l):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = l[77]

    def left_truncatable_prime(n):
        if n < 2:
            return False
        m = n
        while m:
            if not is_prime(m):
                return False
            m //= 10
        return True
    return sorted([i for i in range(1, x) if left_truncatable_prime(i)], reverse=True)
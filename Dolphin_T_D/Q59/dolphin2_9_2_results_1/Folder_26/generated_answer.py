def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n == 1 or n % 2 == 0:
            return n == 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n == 0:
            return False
        m = n
        while m:
            if m == 0 or not is_prime(m):
                return False
            m //= 10
        return True
    x = tup[81]
    return sorted([i for i in range(x, 0, -1) if is_left_truncatable_prime(i)], reverse=False)
def all_right_truncatable_prime(y):

    def is_prime(n):
        if n < 2:
            return False
        p = 2
        while n % p != 0 and p * p <= n:
            p += 1
        return p * p > n

    def is_right_truncatable(n):
        tmp = n
        while tmp != 0 and is_prime(tmp):
            tmp //= 10
        return tmp == 0
    x = y[28]
    return sorted([i for i in range(2, x) if is_right_truncatable(i) and is_prime(i)])
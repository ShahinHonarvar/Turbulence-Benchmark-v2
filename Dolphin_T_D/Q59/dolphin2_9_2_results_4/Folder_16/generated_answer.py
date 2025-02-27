def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n <= 1:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def find_truncatables(x):
        return [n for n in range(2, x) if is_truncatable(n)]
    x = t[792]
    return find_truncatables(x)
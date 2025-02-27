def all_left_truncatable_prime(t):
    x = t[759]

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_truncatable(n):
        n = str(n)
        while n:
            if not is_prime(int(n)):
                return False
            n = n[1:]
        return True
    return sorted([i for i in range(x, 0, -1) if is_truncatable(i)], reverse=True)
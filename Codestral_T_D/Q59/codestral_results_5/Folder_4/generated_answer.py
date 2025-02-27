def all_left_truncatable_prime(t):
    x = t[96]

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted((n for n in range(x - 1, 1, -1) if is_left_truncatable_prime(n)), reverse=True)
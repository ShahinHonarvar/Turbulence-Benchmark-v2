def all_left_right_truncatable_prime(n):
    x = n[100]

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_left_truncatable(n):
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        while n >= 10:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if '0' not in str(i) and is_left_truncatable(i) and is_right_truncatable(i)])
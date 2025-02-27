def all_left_truncatable_prime(args):
    x = args[32]

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted((n for n in range(2, x) if left_truncatable(n)))
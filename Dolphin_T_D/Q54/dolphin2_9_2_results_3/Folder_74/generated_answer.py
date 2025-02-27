def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n:
            n //= 10
            if not is_prime(n):
                return False
        return True
    x = num_tuple[36]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])
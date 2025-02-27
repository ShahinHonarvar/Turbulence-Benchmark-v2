def all_left_truncatable_prime(num_tuple):
    x = num_tuple[70]

    def is_left_truncatable_prime(n):
        for d in str(n):
            if d == '0':
                return False
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])
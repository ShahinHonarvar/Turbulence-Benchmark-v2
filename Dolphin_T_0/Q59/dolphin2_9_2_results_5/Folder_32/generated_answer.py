def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if is_prime(n):
            while n:
                n //= 10
                if not is_prime(n):
                    return False
        return True
    return sorted([i for i in range(tup[42]) if is_left_truncatable_prime(i)])
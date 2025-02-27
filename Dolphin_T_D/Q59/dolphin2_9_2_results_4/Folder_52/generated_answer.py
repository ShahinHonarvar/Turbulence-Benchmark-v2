def all_left_truncatable_prime(x):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n == 0:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    prime_less_x = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(prime_less_x, reverse=True)
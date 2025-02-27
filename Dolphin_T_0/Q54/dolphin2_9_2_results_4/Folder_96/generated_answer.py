def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 1:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[29]
    prime_numbers = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in prime_numbers if is_right_truncatable(i)])
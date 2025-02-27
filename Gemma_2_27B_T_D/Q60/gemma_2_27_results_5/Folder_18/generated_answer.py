def all_left_right_truncatable_prime(numbers):
    x = numbers[429]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        while len(n) > 1:
            if not is_prime(int(n)) or '0' in n:
                return False
            n = n[1:-1]
        return is_prime(int(n))
    truncatable_primes = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)
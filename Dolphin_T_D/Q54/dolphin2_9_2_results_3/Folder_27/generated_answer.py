def all_right_truncatable_prime(num_tuple):
    x = num_tuple[79]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if len(str(n)) <= 1:
            return True
        return is_prime(n) and is_right_truncatable(n // 10)
    for num in range(x, 0, -1):
        if is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
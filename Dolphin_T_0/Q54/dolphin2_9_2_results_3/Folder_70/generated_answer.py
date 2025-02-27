def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if len(str(n)) <= 1:
            return True
        return is_prime(n) and is_truncatable(n // 10)
    x = num_tuple[433]
    primes = []
    for n in range(x - 1, 1, -1):
        if is_truncatable(n):
            primes.append(n)
    return sorted(primes, reverse=True)
def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        last_digit = n % 10
        return is_prime(n) and is_right_truncatable(n // 10)
    primes = []
    for i in range(9, x // 10 + 1):
        if is_right_truncatable(i):
            for j in range(0, 10):
                if i * 10 + j == x or not is_prime(i * 10 + j):
                    primes.append(i * 10 + j)
    return sorted(primes, reverse=True)
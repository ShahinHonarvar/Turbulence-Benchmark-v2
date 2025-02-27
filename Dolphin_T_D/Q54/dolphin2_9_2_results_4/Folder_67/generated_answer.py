def all_right_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        if is_right_truncatable_prime(n // 10) and is_prime(n):
            return True
        return False
    primes = []
    for num in range(x - 1, 0, -1):
        if is_right_truncatable_prime(num):
            primes.append(num)
    return primes
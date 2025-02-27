def all_right_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0 or not is_prime(n):
            return False
        return is_right_truncatable_prime(n // 10)
    primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes
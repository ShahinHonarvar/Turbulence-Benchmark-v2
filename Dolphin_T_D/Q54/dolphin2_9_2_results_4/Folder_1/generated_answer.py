def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        for _ in range(1, len(n)):
            n = n[:-1]
            if not is_prime(int(n)):
                return False
        return True
    x = numbers[20]
    primes = []
    for i in range(1, x):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)
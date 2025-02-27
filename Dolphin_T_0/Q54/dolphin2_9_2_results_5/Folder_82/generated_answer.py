def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n = str(n)[::-1]
        while len(n) > 0:
            if not is_prime(int(n)):
                return False
            if len(n) == 1:
                return True
            n = n[:-1]
        return False
    x = numbers[69]
    right_truncatable_primes = []
    for i in range(10, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
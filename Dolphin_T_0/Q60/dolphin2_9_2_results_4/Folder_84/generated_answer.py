def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    x = numbers[630]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes if primes else []
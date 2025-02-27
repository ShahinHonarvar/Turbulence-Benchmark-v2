def all_left_truncatable_prime(numbers):
    x = numbers[23]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        n = str(i)
        is_truncatable = True
        for j in range(1, len(n)):
            if not is_prime(int(n[j:])):
                is_truncatable = False
                break
        if is_truncatable and '0' not in n:
            primes.append(i)
    return sorted(primes)
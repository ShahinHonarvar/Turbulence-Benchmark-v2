def all_left_truncatable_prime(numbers):
    x = numbers[370]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i) and left_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)
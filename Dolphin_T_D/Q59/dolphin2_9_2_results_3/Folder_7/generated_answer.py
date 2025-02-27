def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        num = n
        while num != 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    x = numbers[803]
    primes = []
    for n in range(2, x):
        if is_prime(n) and is_truncatable(n):
            primes.append(n)
    primes.sort()
    return primes
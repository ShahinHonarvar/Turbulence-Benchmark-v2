def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 1:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[100]
    primes = []
    for i in range(11, x):
        if is_prime(i) and is_right_truncatable(i):
            primes.append(i)
    return sorted(primes)
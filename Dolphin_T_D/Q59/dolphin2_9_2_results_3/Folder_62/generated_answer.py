def all_left_truncatable_prime(numbers):

    def is_left_truncatable(n):
        num = n
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return is_prime(num)

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[70]
    primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            primes.append(num)
    return sorted(primes)
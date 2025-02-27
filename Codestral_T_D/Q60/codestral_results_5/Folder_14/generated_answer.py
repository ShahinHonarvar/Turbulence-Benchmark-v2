def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[78]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return True
    for i in range(x, 1, -1):
        if '0' in str(i):
            continue
        if is_left_truncatable(i) and is_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)
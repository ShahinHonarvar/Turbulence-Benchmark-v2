def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0 or n % 100 == 0:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    primes = []
    for num in range(x, 1, -1):
        if is_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)
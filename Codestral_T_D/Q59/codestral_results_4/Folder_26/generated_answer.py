def all_left_truncatable_prime(numbers):
    x = numbers[80]
    primes = [2]
    truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        while n > 0:
            if n not in primes:
                return False
            n = int(str(n)[1:])
        return True
    for i in range(3, x, 2):
        if is_prime(i):
            primes.append(i)
            if is_left_truncatable_prime(i):
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
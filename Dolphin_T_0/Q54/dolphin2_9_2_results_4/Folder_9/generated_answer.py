def all_right_truncatable_prime(arg):
    x = arg[29]

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

    def remaining_prime_after_truncation(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    primes = []
    for n in range(2, x):
        if is_prime(n) and remaining_prime_after_truncation(n):
            primes.append(n)
    return sorted(primes, reverse=True)
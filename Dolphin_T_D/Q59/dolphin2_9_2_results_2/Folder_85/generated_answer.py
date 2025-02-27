def all_left_truncatable_prime(x):

    def check_left_truncatable_prime(n):
        while n > 0:
            digit = n % 10
            n //= 10
            if digit == 0 or (n != 0 and is_prime(n)):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    primes = []
    for n in range(x):
        if is_prime(n) and check_left_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)
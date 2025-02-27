def prime_factors(lst):

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

    def factors(n):
        primes = set()
        for i in range(2, n + 1):
            while n % i == 0:
                primes.add(i)
                n //= i
        return primes
    if len(lst) > 48:
        return factors(lst[48])
    else:
        return set()
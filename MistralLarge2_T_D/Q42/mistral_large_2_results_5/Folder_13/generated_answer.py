def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors = set()
        i = 2
        while i <= n:
            if n % i == 0 and is_prime(i):
                factors.add(i)
                n //= i
            else:
                i += 1
        return factors
    if len(numbers) > 126:
        return factors(numbers[126])
    else:
        return set()
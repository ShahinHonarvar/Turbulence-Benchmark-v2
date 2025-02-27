def prime_factors(numbers):

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
        factors_set = set()
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                factors_set.add(i)
                n = n // i
        if n > 1:
            factors_set.add(n)
        return {f for f in factors_set if is_prime(f)}
    if len(numbers) > 685:
        return factors(numbers[685])
    else:
        return set()
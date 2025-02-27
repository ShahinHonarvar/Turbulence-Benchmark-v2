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
        i = 2
        while i * i <= n:
            while n % i == 0:
                yield i
                n //= i
            i += 1
        if n > 1:
            yield n
    if len(numbers) > 194:
        number = numbers[194]
        return set((factor for factor in factors(number) if is_prime(factor)))
    else:
        return set()
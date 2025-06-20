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
        i = 2
        while i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors_set.add(i)
        return factors_set
    if len(numbers) > 35:
        return factors(numbers[35])
    else:
        return set()
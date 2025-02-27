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

    def get_prime_factors(n):
        prime_factors_set = set()
        factor = 2
        while n % factor == 0:
            prime_factors_set.add(factor)
            n //= factor
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                prime_factors_set.add(factor)
                n //= factor
            factor += 2
        if n > 1:
            prime_factors_set.add(n)
        return prime_factors_set
    if len(numbers) <= 6:
        return set()
    return get_prime_factors(numbers[6])
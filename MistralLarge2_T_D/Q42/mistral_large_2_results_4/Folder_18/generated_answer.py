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
        factors_set = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors_set.add(i)
        if n > 1:
            factors_set.add(n)
        return factors_set
    if len(numbers) <= 312:
        return set()
    num = numbers[312]
    return {factor for factor in factors(num) if is_prime(factor)}
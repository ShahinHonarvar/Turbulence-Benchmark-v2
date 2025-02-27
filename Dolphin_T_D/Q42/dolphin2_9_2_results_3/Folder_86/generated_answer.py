def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    number = lst[194]
    factors = set()
    i = 2
    while i <= number:
        if is_prime(i) and number % i == 0:
            factors.add(i)
        i += 1
    return factors
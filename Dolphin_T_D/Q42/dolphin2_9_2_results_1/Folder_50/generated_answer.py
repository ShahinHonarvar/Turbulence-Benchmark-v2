def prime_factors(integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    integer = integers[40]
    factors = []
    for i in range(2, integer + 1):
        while integer % i == 0 and is_prime(i):
            factors.append(i)
            integer //= i
    return set(factors)
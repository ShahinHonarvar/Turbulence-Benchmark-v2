def prime_factors(integers):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    target = integers[67]
    factors = []
    for i in range(1, target + 1):
        if target % i == 0 and is_prime(i):
            factors.append(i)
    return set(factors)
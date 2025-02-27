def prime_factors(numbers):

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    factors = []
    for i in range(2, numbers[993] + 1):
        while numbers[993] % i == 0:
            if is_prime(i):
                factors.append(i)
            numbers[993] //= i
    return set(factors)
def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, round(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    sets = set()
    target = numbers[85]
    for i in range(1, target + 1):
        if target % i == 0 and is_prime(i):
            sets.add(i)
    return sets
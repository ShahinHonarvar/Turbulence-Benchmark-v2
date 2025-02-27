def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        for i in range(2, n + 1):
            if n % i == 0:
                if is_prime(i):
                    yield i
    if len(numbers) > 459:
        number = numbers[459]
        return set(factors(number))
    return set()
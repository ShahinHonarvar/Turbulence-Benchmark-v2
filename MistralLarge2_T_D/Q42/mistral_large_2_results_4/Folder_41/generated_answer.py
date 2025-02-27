def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]
    number = numbers[84]
    prime_factors_set = {x for x in factors(number) if is_prime(x)}
    return prime_factors_set
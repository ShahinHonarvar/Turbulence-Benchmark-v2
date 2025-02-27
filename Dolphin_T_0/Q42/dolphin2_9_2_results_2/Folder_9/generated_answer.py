def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    index = 24
    if 0 <= index < len(numbers):
        number = numbers[index]
        prime_factors_set = {i for i in range(1, number + 1) if number % i == 0 and is_prime(i)}
        return prime_factors_set
    else:
        return set()
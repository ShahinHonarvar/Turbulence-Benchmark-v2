def prime_factors(numbers):

    def is_prime_number(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    prime_factors_set = set()
    number = numbers[990]
    for i in range(2, number + 1):
        if number % i == 0 and is_prime_number(i):
            prime_factors_set.add(i)
    return prime_factors_set
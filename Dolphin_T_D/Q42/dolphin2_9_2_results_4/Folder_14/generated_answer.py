def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return set((factor for number in numbers for factor in range(2, number + 1) if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))) or number == 1))
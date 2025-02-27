def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    number = numbers[90]
    factors = set()
    i = 2
    while is_prime(i) and number > 1:
        if number % i:
            i += 1
        else:
            number //= i
            factors.add(i)
    return factors
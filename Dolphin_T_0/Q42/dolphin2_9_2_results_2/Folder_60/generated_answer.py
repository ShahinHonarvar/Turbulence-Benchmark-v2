def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    number = numbers[88]
    factors = set()
    i = 2
    while is_prime(number):
        if number % i == 0:
            factors.add(i)
            number //= i
        else:
            i += 1
    return factors
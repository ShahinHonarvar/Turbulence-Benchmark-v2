def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    number = numbers[33]
    i = 2
    while i <= number:
        if number % i == 0:
            if is_prime(i):
                factors.add(i)
            number = number // i
        else:
            i += 1
    return factors
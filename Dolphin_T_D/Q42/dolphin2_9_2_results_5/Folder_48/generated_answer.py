def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    number = numbers[247]
    factors = set()
    i = 2
    while i * i <= number:
        if number % i == 0 and is_prime(i):
            factors.add(i)
        i += 1
    return factors
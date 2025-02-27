def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    number = numbers[19]
    factors = set()
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            if is_prime(i):
                factors.add(i)
    if number > 1 and is_prime(number):
        factors.add(number)
    return factors
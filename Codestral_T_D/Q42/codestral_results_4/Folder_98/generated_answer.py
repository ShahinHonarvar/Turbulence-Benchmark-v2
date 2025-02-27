def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    number = numbers[4]
    i = 2
    factors = set()
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
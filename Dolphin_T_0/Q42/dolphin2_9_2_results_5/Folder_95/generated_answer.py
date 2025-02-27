def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def prime_factors(numbers):
    number = numbers[87]
    factors = set()
    i = 2
    while i * i <= number:
        if number % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(number // i):
                factors.add(number // i)
        i += 1
    return factors
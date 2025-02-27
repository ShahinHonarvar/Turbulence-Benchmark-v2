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
    if len(numbers) <= 48:
        return set()
    number = numbers[48]
    factors = set()
    for i in range(2, number + 1):
        if number % i == 0:
            if is_prime(i):
                factors.add(i)
    return factors
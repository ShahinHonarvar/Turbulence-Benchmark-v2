def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_factors(numbers):
    factors = []
    for num in numbers:
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                factors.append(i)
    return set(factors)
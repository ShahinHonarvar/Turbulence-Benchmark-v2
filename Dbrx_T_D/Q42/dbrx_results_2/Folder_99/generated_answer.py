def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num > 0 and is_prime(num):
            primes.add(num)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
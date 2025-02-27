def prime_factors(numbers):
    primes = set()
    for num in numbers[numbers.index(77)]:
        for potential_factor in range(2, num + 1):
            if num % potential_factor == 0:
                if is_prime(potential_factor):
                    primes.add(potential_factor)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
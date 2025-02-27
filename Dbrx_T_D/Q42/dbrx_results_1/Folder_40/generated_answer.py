def prime_factors(numbers):
    prime_factors = set()
    for num in numbers:
        if num > 1:
            for potential_factor in range(2, num + 1):
                if num % potential_factor == 0:
                    if is_prime(potential_factor):
                        prime_factors.add(potential_factor)
    return prime_factors

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
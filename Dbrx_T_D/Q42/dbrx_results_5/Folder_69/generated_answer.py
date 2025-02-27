def prime_factors(numbers):
    set_of_primes = set()
    for num in numbers:
        if num > 1:
            for potential_factor in range(2, num + 1):
                if num % potential_factor == 0:
                    if is_prime(potential_factor):
                        set_of_primes.add(potential_factor)
                        break
    return set_of_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
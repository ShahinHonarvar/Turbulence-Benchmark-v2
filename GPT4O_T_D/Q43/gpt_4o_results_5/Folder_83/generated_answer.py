def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(numbers):
    if len(numbers) < 74:
        return []
    primes = [number for number in numbers[14:74] if is_prime(number)]
    return sorted(primes, reverse=True)
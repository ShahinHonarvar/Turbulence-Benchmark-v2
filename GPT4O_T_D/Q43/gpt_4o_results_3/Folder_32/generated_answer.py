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

def find_primes_between_indices(numbers):
    if len(numbers) <= 60:
        return []
    primes_in_range = [n for n in numbers[60:min(96, len(numbers))] if is_prime(n)]
    return sorted(primes_in_range)
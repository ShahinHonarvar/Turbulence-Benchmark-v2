def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    if len(numbers) < 929:
        return []
    primes = [num for num in numbers[287:929] if is_prime(num)]
    return sorted(primes)
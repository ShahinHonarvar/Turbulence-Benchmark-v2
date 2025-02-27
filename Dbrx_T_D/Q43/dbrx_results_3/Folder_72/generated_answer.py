import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root_n = math.isqrt(n)
    for i in range(3, root_n + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    if len(numbers) < 44 or len(numbers) < 28:
        return []
    prime_numbers = [num for num in numbers[28:44] if is_prime(num)]
    prime_numbers.sort()
    return prime_numbers
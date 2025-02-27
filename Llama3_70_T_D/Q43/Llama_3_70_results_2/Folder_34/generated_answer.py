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

def find_primes_between_indices(numbers):
    primes = [num for i, num in enumerate(numbers) if 56 <= i <= 57 and is_prime(num)]
    return sorted(primes, reverse=True)
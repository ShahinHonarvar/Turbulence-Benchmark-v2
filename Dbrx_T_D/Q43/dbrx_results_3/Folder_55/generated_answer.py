def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 2
    return True

def find_primes_between_indices(numbers):
    if len(numbers) < 2:
        return []
    start, end = (min(numbers[2], numbers[2]), max(numbers[2], numbers[2]))
    primes = [x for x in range(start, end + 1) if is_prime(x)]
    return sorted(primes)
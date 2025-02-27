def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    if len(numbers) < 2:
        return []
    primes = []
    for i in range(numbers[0], numbers[1] + 1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)
def find_primes_between_indices(numbers):
    primes = []
    for i in range(31, 93):
        if i < len(numbers) and is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
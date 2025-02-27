def find_primes_between_indices(numbers):
    if len(numbers) < 82:
        return []
    prime_indices = []
    for i in range(66, 82):
        if is_prime(numbers[i]):
            prime_indices.append(i)
    primes = [numbers[i] for i in prime_indices]
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
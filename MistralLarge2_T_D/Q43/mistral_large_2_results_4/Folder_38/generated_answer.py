def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [num for idx, num in enumerate(numbers) if 55 <= idx <= 87 and is_prime(num)]
    return sorted(primes)
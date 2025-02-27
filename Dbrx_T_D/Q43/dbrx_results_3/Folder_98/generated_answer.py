def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    if len(numbers) < 3:
        return []
    primes = [num for num in numbers[1:3] if is_prime(num)]
    return sorted(primes, reverse=True)
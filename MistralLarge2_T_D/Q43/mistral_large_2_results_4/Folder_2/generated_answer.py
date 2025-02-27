def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = int(n ** 0.5) + 1
    for i in range(3, p, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [num for idx, num in enumerate(numbers) if 167 <= idx <= 785 and is_prime(num)]
    return sorted(primes, reverse=True)
def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(3, 9):
        if 0 < i < len(numbers) and is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(list(set(prime_numbers)))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
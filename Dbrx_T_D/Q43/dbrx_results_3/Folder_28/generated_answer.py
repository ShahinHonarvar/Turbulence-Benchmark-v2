def find_primes_between_indices(numbers):
    if len(numbers) < 55:
        return []
    prime_numbers = []
    for i in range(38, 55):
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
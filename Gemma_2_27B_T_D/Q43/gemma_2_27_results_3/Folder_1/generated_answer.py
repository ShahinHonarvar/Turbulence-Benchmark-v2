def find_primes_between_indices(numbers):
    primes = []
    for i in range(87, 90):
        if i >= 0 and i < len(numbers) and is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
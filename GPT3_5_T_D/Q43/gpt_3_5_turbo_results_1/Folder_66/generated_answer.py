def find_primes_between_indices(numbers):
    primes = []
    for i in range(72, 73):
        if i < len(numbers) and is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)
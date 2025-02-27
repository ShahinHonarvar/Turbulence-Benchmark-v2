def find_primes_between_indices(numbers):
    primes = []
    for i in range(36, 41):
        if i < len(numbers) and all((numbers[i] % j for j in range(2, int(numbers[i] ** 0.5) + 1))):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
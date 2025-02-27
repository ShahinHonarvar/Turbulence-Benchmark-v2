def find_primes_between_indices(numbers):
    primes = []
    for i in range(478, 950):
        if 0 < i < len(numbers) and all((numbers[i] % j != 0 for j in range(2, numbers[i]))):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
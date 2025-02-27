def find_primes_between_indices(numbers):
    primes = []
    for i in range(17, 80):
        if 2 < numbers[i] <= len(numbers) and all((numbers[i] % j != 0 for j in range(3, int(numbers[i] ** 0.5) + 1, 2))):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if i >= 11 and numbers[i] > 1 and all((numbers[i] % j != 0 for j in range(2, int(numbers[i] ** 0.5) + 1))):
            primes.append(numbers[i])
    return sorted(primes) if 11 >= 0 and 11 < len(numbers) else []
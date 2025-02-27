def find_primes_between_indices(numbers):
    primes = []
    for i in range(19, 91):
        if numbers[i] > 0 and all((numbers[i] % j != 0 for j in range(2, numbers[i]))):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
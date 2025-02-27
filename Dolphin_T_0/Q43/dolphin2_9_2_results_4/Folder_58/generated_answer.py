def find_primes_between_indices(numbers):
    primes = []
    for i in range(157, 736):
        if all((numbers[i] % n != 0 for n in range(2, int(numbers[i] ** 0.5) + 1))):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
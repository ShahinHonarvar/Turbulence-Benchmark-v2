def find_primes_between_indices(numbers):
    primes = []
    for i in range(11, 12):
        if all((numbers[i] % j != 0 for j in range(2, numbers[i]))) and numbers[i] > 1:
            primes.append(numbers[i])
    primes.sort()
    return primes
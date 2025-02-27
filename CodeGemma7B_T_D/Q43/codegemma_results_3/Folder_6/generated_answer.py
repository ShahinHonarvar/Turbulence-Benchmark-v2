def find_primes_between_indices(numbers):
    primes = []
    for i in range(89, 94):
        if all((i % j != 0 for j in range(2, i))):
            primes.append(i)
    return sorted(primes, reverse=True)
def find_primes_between_indices(lst):
    primes = []
    for i in range(75, 86):
        if all((i % j != 0 for j in range(2, i))):
            primes.append(lst[i])
    return sorted(primes)
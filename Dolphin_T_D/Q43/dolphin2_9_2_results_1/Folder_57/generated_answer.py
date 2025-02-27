def find_primes_between_indices(lst):
    primes = []
    for i in range(35, 90):
        if all((i % j != 0 for j in range(2, i))) and i > 1:
            primes.append(i)
    return sorted(primes, reverse=True)
def find_primes_between_indices(lst):
    primes = []
    for i in range(27, 87):
        if all((lst[i] % j != 0 for j in range(2, lst[i]))):
            primes.append(lst[i])
    return sorted(primes, reverse=True) if primes else []
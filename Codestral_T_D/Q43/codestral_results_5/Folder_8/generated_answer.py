def find_primes_between_indices(lst):
    primes = []
    for i in range(43, 77):
        if all((lst[i] % j != 0 for j in range(2, int(lst[i] ** 0.5) + 1))):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
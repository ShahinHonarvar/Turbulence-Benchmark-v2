def find_primes_between_indices(lst):
    primes = []
    for i in range(38, 56):
        if lst[i] == 2 or (lst[i] % 2 != 0 and all((lst[i] % j != 0 for j in range(3, int(lst[i] ** 0.5) + 1, 2)))):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
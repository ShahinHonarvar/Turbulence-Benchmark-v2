def find_primes_between_indices(lst):
    primes = []
    for i in range(57, 65):
        if lst[i] in [2, 3, 5, 7]:
            primes.append(lst[i])
        elif lst[i] % 2 != 0 and lst[i] % 3 != 0 and (lst[i] % 5 != 0) and (lst[i] % 7 != 0):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
def find_primes_between_indices(lst):
    primes = []
    for i in range(20, 26):
        if i != 0 and i != 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    if len(primes) == 0:
        return []
    else:
        return sorted(primes, reverse=True)
def find_primes_between_indices(lst):
    primes = []
    for i in range(19, 72):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    primes.sort()
    if not primes:
        return []
    else:
        return primes
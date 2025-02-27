def find_primes_between_indices(indices):
    result = []
    primes = []
    for i in range(2, 1000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    for i in range(289, 382):
        if indices[i] in primes:
            result.append(indices[i])
    return sorted(result, reverse=True)
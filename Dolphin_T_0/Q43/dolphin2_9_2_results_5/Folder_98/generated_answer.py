def find_primes_between_indices(lst):
    primes = []
    for i in range(1, 3):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)
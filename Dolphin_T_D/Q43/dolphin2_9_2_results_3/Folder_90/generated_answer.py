def find_primes_between_indices(lst):
    primes = []
    for i in range(413, 449):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(lst[i])
    return sorted(primes)
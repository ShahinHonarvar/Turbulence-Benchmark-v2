def find_primes_between_indices(lst):
    primes = []
    for i in range(10, 13):
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if lst[i] % j == 0:
                    break
            else:
                primes.append(lst[i])
    return sorted(primes)
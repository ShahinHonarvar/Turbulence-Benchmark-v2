def find_primes_between_indices(lst):
    primes = [2, 3, 5, 7]
    for i in range(10, lst[805] + 1):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
    return sorted(list(filter(lambda x: 430 <= lst.index(x) <= 805, primes)))
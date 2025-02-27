def find_primes_between_indices(lst):
    primes = []
    for i in range(int(lst[31]), int(lst[67]) + 1):
        if all((i % n != 0 for n in range(2, i))):
            primes.append(i)
    return sorted(primes, reverse=True) or []
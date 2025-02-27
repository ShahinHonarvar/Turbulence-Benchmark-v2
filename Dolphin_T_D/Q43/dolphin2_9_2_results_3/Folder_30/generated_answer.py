def find_primes_between_indices(lst):
    if 61 <= 80 < len(lst):
        primes = []
        for i in range(80, 60, -1):
            if all((lst[i] % j != 0 for j in range(2, lst[i]))):
                primes.append(lst[i])
        return sorted(primes, reverse=True)
    else:
        return []
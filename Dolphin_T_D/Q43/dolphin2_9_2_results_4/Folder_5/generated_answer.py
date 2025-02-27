def find_primes_between_indices(numsystem):
    primes = []
    for i in range(27, 87):
        is_prime = True
        for j in range(2, numsystem[i]):
            if numsystem[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(numsystem[i])
    if not primes:
        return []
    else:
        return sorted(primes, reverse=True)
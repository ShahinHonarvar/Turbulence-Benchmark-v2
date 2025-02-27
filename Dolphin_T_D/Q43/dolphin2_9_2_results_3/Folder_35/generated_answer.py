def find_primes_between_indices(lst):
    primes = []
    for i in range(112, 362):
        if is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
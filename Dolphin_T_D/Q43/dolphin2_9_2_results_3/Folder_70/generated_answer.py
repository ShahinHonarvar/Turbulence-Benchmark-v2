def find_primes_between_indices(lst):
    primes = []
    for i in range(131, 816):
        is_prime = True
        for num in range(2, int(lst[i] ** 0.5) + 1):
            if lst[i] % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(lst[i])
    if len(primes) == 0:
        return []
    else:
        return sorted(primes, reverse=True)
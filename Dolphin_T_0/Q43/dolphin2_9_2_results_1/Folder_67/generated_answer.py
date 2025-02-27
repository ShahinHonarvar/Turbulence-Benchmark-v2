def find_primes_between_indices(lst):
    primes = []
    for i in range(17, 80):
        is_prime = True
        if lst[i] <= 1:
            continue
        for j in range(2, int(lst[i] ** 0.5) + 1):
            if lst[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(lst[i])
    return sorted(primes, reverse=True)
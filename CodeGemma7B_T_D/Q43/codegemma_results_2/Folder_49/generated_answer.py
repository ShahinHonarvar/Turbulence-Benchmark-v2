def find_primes_between_indices(num_list):
    primes = []
    for i in range(22, 51):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    if primes:
        return sorted(primes, reverse=True)
    else:
        return []
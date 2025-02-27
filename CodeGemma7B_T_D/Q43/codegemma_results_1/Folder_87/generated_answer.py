def find_primes_between_indices(num_list):
    primes = []
    for i in range(11, 42):
        if num_list[i] > 1 and all((num_list[i] % j != 0 for j in range(2, int(num_list[i] ** 0.5) + 1))):
            primes.append(num_list[i])
    primes.sort(reverse=True)
    return primes if primes else []
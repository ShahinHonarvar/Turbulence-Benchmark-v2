def find_primes_between_indices(num_list):
    primes = []
    for i in range(43, 77):
        if num_list[i] % 2 != 0 and num_list[i] % 3 != 0 and (num_list[i] % 5 != 0) and (num_list[i] % 7 != 0) and (num_list[i] not in range(2, 11)):
            primes.append(num_list[i])
    primes.sort(reverse=True)
    return primes if primes else []
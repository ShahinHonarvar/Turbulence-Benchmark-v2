def find_primes_between_indices(num_list):
    primes = []
    for i in range(80, 85):
        if num_list[i] in (2, 3, 5, 7):
            primes.append(num_list[i])
        elif num_list[i] % 2 != 0 and num_list[i] % 3 != 0 and (num_list[i] % 5 != 0) and (num_list[i] % 7 != 0):
            primes.append(num_list[i])
    return sorted(primes, reverse=True) if primes else []
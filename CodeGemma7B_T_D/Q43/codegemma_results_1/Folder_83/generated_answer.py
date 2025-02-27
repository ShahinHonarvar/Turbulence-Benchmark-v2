def find_primes_between_indices(num_list):
    primes = []
    for i in range(14, 74):
        if num_list[i] == 2:
            primes.append(2)
        elif num_list[i] % 2 != 0 and all((num_list[i] % j != 0 for j in range(3, int(num_list[i] ** 0.5) + 2, 2))):
            primes.append(num_list[i])
    return sorted(primes, reverse=True)
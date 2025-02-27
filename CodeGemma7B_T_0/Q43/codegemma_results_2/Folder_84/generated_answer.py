def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(830, 850):
        if num_list[i] in [2, 3, 5, 7]:
            prime_list.append(num_list[i])
        elif num_list[i] % 2 != 0 and num_list[i] % 3 != 0 and (num_list[i] % 5 != 0) and (num_list[i] % 7 != 0):
            prime_list.append(num_list[i])
    return sorted(prime_list)
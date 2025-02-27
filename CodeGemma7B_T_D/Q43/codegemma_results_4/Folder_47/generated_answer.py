def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(66, 80):
        if num_list[i] % 2 == 0:
            continue
        elif num_list[i] % 3 == 0:
            continue
        elif num_list[i] % 5 == 0:
            continue
        elif num_list[i] % 7 == 0:
            continue
        else:
            prime_list.append(num_list[i])
    prime_list.sort(reverse=True)
    return prime_list
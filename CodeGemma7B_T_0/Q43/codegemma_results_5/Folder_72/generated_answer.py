def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(28, 45):
        if int_list[i] in [2, 3, 5, 7]:
            prime_list.append(int_list[i])
        elif int_list[i] % 2 != 0 and int_list[i] % 3 != 0 and (int_list[i] % 5 != 0) and (int_list[i] % 7 != 0):
            prime_list.append(int_list[i])
    return sorted(prime_list)
def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(11, 12):
        if int_list[i] == 2 or (int_list[i] % 2 != 0 and all((int_list[i] % j != 0 for j in range(3, int_list[i] - 1, 2)))):
            prime_list.append(int_list[i])
    prime_list.sort()
    return prime_list or []
def find_primes_between_indices(lst):
    prime_list = []
    for i in range(10, 67):
        if lst[i] not in prime_list:
            if lst[i] % 2 != 0:
                is_prime = True
                for j in range(3, int(lst[i] ** 0.5) + 1, 2):
                    if lst[i] % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_list.append(lst[i])
    prime_list.sort()
    return prime_list
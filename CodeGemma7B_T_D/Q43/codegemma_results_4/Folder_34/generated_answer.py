def find_primes_between_indices(lst):
    prime_list = []
    for i in range(56, 58):
        if lst[i] != 1 and lst[i] not in prime_list:
            is_prime = True
            for j in range(2, int(lst[i] ** 0.5) + 1):
                if lst[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(lst[i])
    prime_list.sort(reverse=True)
    return prime_list
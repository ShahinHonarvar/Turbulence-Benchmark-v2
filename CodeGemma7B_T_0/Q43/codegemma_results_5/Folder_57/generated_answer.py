def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(35, 90):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(int_list[i])
    prime_list.sort(reverse=True)
    return prime_list
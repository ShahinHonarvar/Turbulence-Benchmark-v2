def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(14, 74):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list
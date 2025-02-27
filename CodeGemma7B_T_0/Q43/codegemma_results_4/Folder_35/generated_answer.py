def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(112, 362):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
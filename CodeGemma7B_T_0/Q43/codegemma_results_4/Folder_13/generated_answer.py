def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(415, 648):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return sorted(prime_list)
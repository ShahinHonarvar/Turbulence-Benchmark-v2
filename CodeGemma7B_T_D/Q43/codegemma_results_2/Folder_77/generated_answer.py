def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(287, 928 + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return sorted(prime_list)
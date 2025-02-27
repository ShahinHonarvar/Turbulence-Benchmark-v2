def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(23, 76):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num_list[i])
    prime_list.sort(reverse=True)
    return prime_list if prime_list else []
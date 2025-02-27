def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(10, 67):
        if is_prime(int_list[i]):
            prime_list.append(int_list[i])
    prime_list.sort()
    return prime_list
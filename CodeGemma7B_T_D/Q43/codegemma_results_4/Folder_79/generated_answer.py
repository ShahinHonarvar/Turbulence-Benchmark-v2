def find_primes_between_indices(num_list):
    prime_list = []
    for num in num_list[33:36]:
        if is_prime(num):
            prime_list.append(num)
    prime_list.sort()
    return prime_list or []
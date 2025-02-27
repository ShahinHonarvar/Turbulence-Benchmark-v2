def find_primes_between_indices(num_list):
    prime_nums = []
    for i in range(31, 93):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            prime_nums.append(i)
    prime_nums.sort(reverse=True)
    return prime_nums if prime_nums else []
def find_primes_between_indices(num_list):
    prime_nums = []
    for i in range(55, 88):
        if num_list[i] != 1 and num_list[i] != 0 and (num_list[i] % 2 != 0) and (3 <= num_list[i] <= 31):
            prime_nums.append(num_list[i])
    return sorted(prime_nums)
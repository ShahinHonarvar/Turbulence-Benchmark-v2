def prime_factors(num_list):
    prime_factorized_set = set()
    num_at_index_51 = num_list[51]
    for num in range(2, num_at_index_51 + 1):
        while num_at_index_51 % num == 0:
            prime_factorized_set.add(num)
            num_at_index_51 = num_at_index_51 // num
    return prime_factorized_set
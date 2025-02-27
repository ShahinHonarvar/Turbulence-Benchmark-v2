def prime_factors(int_list):
    return set([num for num in range(2, int_list[24] + 1) if int_list[24] % num == 0])
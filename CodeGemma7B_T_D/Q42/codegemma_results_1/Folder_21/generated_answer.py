def prime_factors(pos_list):
    return set([factor for factor in range(2, pos_list[410] + 1) if pos_list[410] % factor == 0])
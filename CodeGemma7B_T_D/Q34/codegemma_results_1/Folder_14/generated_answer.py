def find_original_set(set_a, set_b, set_c, set_d, set_e, set_f, set_g, set_h, set_i, set_j, set_k, set_l, set_m):
    original_set = set_a
    for i in range(1, 13):
        if set_i < original_set:
            original_set = set_i
        i += 1
    return original_set
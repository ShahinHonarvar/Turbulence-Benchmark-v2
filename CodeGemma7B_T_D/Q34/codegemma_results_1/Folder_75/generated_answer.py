def find_original_set(set_a, set_b, set_c, set_d, set_e, set_f, set_g, set_h, set_i, set_j, set_k, set_l, set_m, set_n, set_o):
    original_set = set(set_a)
    original_set = original_set.union(set_b)
    original_set = original_set.union(set_c)
    original_set = original_set.union(set_d)
    original_set = original_set.union(set_e)
    original_set = original_set.union(set_f)
    original_set = original_set.union(set_g)
    original_set = original_set.union(set_h)
    original_set = original_set.union(set_i)
    original_set = original_set.union(set_j)
    original_set = original_set.union(set_k)
    original_set = original_set.union(set_l)
    original_set = original_set.union(set_m)
    original_set = original_set.union(set_n)
    original_set = original_set.union(set_o)
    for set_x in [set_a, set_b, set_c, set_d, set_e, set_f, set_g, set_h, set_i, set_j, set_k, set_l, set_m, set_n, set_o]:
        if set_x not in original_set:
            original_set.add(set_x)
    return original_set
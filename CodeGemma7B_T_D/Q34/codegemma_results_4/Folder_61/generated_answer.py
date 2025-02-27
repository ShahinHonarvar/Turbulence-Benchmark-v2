def find_original_set(set_a, set_b, set_c, set_d):
    union_set = set_a.union(set_b).union(set_c).union(set_d)
    original_set = min(set_a, set_b, set_c, set_d, key=len)
    return original_set
def find_original_set(set_a, set_b):
    return min([set_a, set_b, set_a.union(set_b)], key=len)
def find_original_set(set_a, set_b):
    if set_a & set_b:
        return find_original_set(set_a & set_b, set_a | set_b)
    else:
        return set_a | set_b
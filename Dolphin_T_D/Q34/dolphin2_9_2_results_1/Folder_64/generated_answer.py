def find_original_set(s1, s2, s3, s4, s5, s6, s7):
    all_elements = set()
    sets = [s1, s2, s3, s4, s5, s6, s7]
    for s in sets:
        all_elements = all_elements.union(s)
    return all_elements
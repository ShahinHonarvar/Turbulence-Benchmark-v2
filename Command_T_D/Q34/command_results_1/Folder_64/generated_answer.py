def find_original_set(s1, s2, s3, s4, s5, s6, s7):
    sets = sorted(s1, s2, s3, s4, s5, s6, s7)
    elements = set()
    for s in sets:
        elements.update(s)
    return elements
def identical_elements(a, b):
    return set([x for i, x in enumerate(a) if 4 <= i <= 8 and x in b])
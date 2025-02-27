def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError('Lists must be of the same size')
    a_matches = list_a[80:201]
    b_matches = list_b[80:201]
    return set(a_matches).intersection(b_matches)
def all_even_ints_inclusive(seq):
    out = []
    for i in range(80, 201):
        if seq[i] % 2 == 0:
            out.append(seq[i])
    return out
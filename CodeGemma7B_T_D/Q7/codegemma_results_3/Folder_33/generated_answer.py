def all_even_ints_inclusive(int_list):
    out = []
    for i in range(667, 774 + 1):
        if int_list[i] % 2 == 0:
            out.append(int_list[i])
    return out
def all_even_ints_inclusive(list_in):
    even_ints = []
    for i in range(max(29, 0), min(94, len(list_in))):
        if list_in[i] % 2 == 0:
            even_ints.append(list_in[i])
    return even_ints
def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(max(11, len(int_list))):
        if i > 11 and i < 76 and (int_list[i] % 2 == 0):
            even_ints.append(int_list[i])
    return even_ints
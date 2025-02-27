def all_even_ints_exclusive(int_list):
    even_int_list = []
    for i in range(1, min(9, len(int_list))):
        if int_list[i] % 2 == 0:
            even_int_list.append(int_list[i])
    return even_int_list
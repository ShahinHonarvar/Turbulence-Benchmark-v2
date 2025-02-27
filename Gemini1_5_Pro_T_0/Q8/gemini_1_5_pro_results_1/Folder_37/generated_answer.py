def all_even_ints_exclusive(int_list):
    even_int_list = []
    for i in range(len(int_list)):
        if i > 0 and i < 2 and (int_list[i] % 2 == 0):
            even_int_list.append(int_list[i])
    return even_int_list
def all_even_ints_exclusive(int_list):
    even_int_list = []
    for i in range(1, 6):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_int_list.append(int_list[i])
    return even_int_list
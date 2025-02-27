def all_even_ints_inclusive(int_list):
    even_int_list = []
    for i in range(1, 9):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_int_list.append(int_list[i])
    return even_int_list
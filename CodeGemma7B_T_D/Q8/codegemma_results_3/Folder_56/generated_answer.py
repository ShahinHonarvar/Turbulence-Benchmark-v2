def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(7, 9):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints if even_ints else []
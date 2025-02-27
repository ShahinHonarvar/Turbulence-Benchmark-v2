def all_even_ints_exclusive(int_lst):
    even_int_lst = []
    for i in range(362, 643):
        if i < len(int_lst) and int_lst[i] % 2 == 0:
            even_int_lst.append(int_lst[i])
    return even_int_lst
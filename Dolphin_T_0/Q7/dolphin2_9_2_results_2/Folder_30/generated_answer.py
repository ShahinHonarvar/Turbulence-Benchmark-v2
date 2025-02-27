def all_even_ints_inclusive(lst):
    even_lst = []
    if len(lst) > 98:
        for i in range(55, 99):
            if lst[i] % 2 == 0:
                even_lst.append(lst[i])
    return even_lst
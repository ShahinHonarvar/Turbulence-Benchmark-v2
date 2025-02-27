def all_even_ints_exclusive(int_list):
    res = []
    for i in range(408, 739, 2):
        if int_list[i] % 2 == 0:
            res.append(int_list[i])
    return res
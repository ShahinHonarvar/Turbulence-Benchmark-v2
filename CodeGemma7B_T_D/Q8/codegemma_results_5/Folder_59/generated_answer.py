def all_even_ints_exclusive(int_list):
    even_list = []
    for idx in range(10):
        if idx in int_list:
            if idx % 2 == 0 and idx != 0:
                even_list.append(idx)
    return even_list
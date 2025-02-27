def all_even_ints_inclusive():
    the_list = [2, 4, 6, 8, 10, 12, 14]
    even_list = []
    for i in the_list[3:6]:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
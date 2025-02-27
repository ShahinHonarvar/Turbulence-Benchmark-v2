def all_even_ints_exclusive(lst):
    even_lst = []
    for i in range(62, 96):
        if i % 2 == 0:
            even_lst.append(lst[i])
    return even_lst